import requests
import time
from bs4 import BeautifulSoup
import logging
import threading
import pymysql

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }
    def __init__(self,filename,level='info'):
        self.logger = logging.getLogger(filename)
        LOG_FORMAT = '%(asctime)s - Thread[%(thread)s=%(threadName)s] - %(filename)s[L%(lineno)d] - %(levelname)s: %(message)s'
        format_str = logging.Formatter(LOG_FORMAT)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = logging.FileHandler(filename=filename,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)

log = Logger('readfree.log',level='debug')

# 通用数据
class CommonData:
    def __init__(self):
        self.check_url = 'http://readfree.me/accounts/checkin'
        self.cookieContent = "sessionid=fvkw046jeslicx5ku5ns5nd1wofkpv9i;csrftoken=K5cXO6TQ5QJU3rxS3u8p9KW6qMAtQj7iqS2LqMSarDmuOJANSxh9vIsJ9DzOsiCs; Hm_lvt_375aa6d601368176e50751c1c6bf0e82=1541646641,1542005925,1542072758,1542159932; Hm_lpvt_375aa6d601368176e50751c1c6bf0e82=%s"%(int(time.time()))
        self.cookie = {}
        for line in self.cookieContent.split(';'):
            name, value = line.strip().split('=', 1)
            self.cookie[name] = value

def connect_readfree_db():
    return pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='222222',
                           database='readfree',
                           charset='utf8')

def get_by_booklink(book_link):
    conn = connect_readfree_db()
    cursor = conn.cursor()
    cursor.execute(("SELECT  * FROM book where book_link = \'%s\'") % book_link)
    row = cursor.rowcount
    result = cursor.fetchall()
    # print(row)
    # print(len(result))
    # print(result)
    return row

def insert_book_check(book):
    row = get_by_booklink(book['book_link'])
    if row == 0:
        insert_data('book',book)

def insert_book(book):
    insert_data('book', book)

def insert_data(table,data_dict):
    try:
        data_values = "(" + "%s," * (len(data_dict)) + ")"
        data_values = data_values.replace(',)', ')')
        dbField = data_dict.keys()
        dataTuple = tuple(data_dict.values())
        dbField = str(tuple(dbField)).replace("'",'')
        conn = connect_readfree_db()
        cursor = conn.cursor()
        sql = """ insert into %s %s values %s """ % (table,dbField,data_values)
        params = dataTuple
        # print(sql)
        # print(params)
        cursor.execute(sql, params)
        conn.commit()
        cursor.close()
        return 1
    except Exception as e:
        log.logger.error(e)
        return 0

# 登录签到
def checkin(url,cookie):
    res = requests.get(url, cookies=cookie)

class ThreadLoad(threading.Thread):
    def __init__(self, seq, threadName, dataQueue, cookie, threadNum):
        super(ThreadLoad, self).__init__()
        self.threadName = threadName
        self.seq = seq
        self.dataQueue = dataQueue
        self.cookie = cookie
        self.threadNum = threadNum

    def run(self):
        total = 5070
        max = total//self.threadNum
        for i in range(max):
            page = i*self.threadNum+self.seq
            if page <= total:
                self.loadPageBook(page)

    # 读取某页图书信息
    def loadPageBook(self,page):
        # log.logger.info("正在读取页码[%s]的图书信息……"%str(page))
        page_url = 'http://readfree.me/?page='+str(page)
        html = requests.get(page_url,cookies=self.cookie)
        bs_obj = BeautifulSoup(html.content,'html.parser')
        book_item_list = bs_obj.find_all('li','book-item')
        # print(bs_obj)
        # print(len(book_item_list))
        #for item in book_item_list:
        for k in range(len(book_item_list)):
            item = book_item_list[k]
            book = {}
            book_info = item.find('div','book-info')
            aa = book_info.find('a','pjax')
            meta = item.find('div','book-meta muted')
            score = meta.find('span','badge badge-success').get_text()
            # print(aa)
            book['book_link'] = aa.get('href')
            book['name'] = aa.get_text().strip()
            existed = get_by_booklink(book['book_link']) > 0
            if existed:
                log.logger.info("图书[%s][%s]已经采集过……" % (book['book_link'],book['name']))
                continue
            book['score'] = float(score)
            book_url = 'http://readfree.me'+aa.get('href')+'?_pjax=%23pjax'
            book_html = requests.get(book_url,cookies=self.cookie)
            book_obj = BeautifulSoup(book_html.content, 'html.parser')
            # print(book_obj)
            douban_obj = book_obj.find('span','badge badge-success')
            douban_url = ''
            if douban_obj is not None:
                douban_url = douban_obj.parent.find('a').get('href')
            book['douban_link'] = douban_url
            down_list = book_obj.find_all('a','book-down btn btn-mini btn-success')
            mobi = []
            pdf = []
            total_down_num = 0
            # 读取该书籍的下载信息列表
            for down in down_list:
                down_href = down.get('href')
                span = down.find('span').get_text()
                down_num=1000
                if span != '1k+':
                    down_num = int(span)
                total_down_num += down_num
                if down_href.find('.mobi') > -1:
                    mobi.append((down_href,down_num))
                if down_href.find('.pdf') > -1:
                    pdf.append((down_href,down_num))
            book['down'] = total_down_num
            mobi = sorted(mobi,key=lambda x:x[1],reverse=True)
            pdf = sorted(pdf,key=lambda x:x[1],reverse=True)
            if len(mobi) > 0:
                book['mobi_most'] = mobi[0][0]
            if len(pdf) > 0:
                book['pdf_most'] = pdf[0][0]
            book['mobi'] = str(mobi)
            book['pdf'] = str(pdf)
            # self.dataQueue.append(book)
            insert_book(book)
            log.logger.info("页码[%s]的[%s]图书信息为：%s"%(str(page),str(k),str(book)))

common = CommonData()
thread_loaders = []
thread_num = 50
for i in range(thread_num):
    name = 'load-thread-'+str(i+1)
    dataQueue = []
    thread = ThreadLoad(i+1,name, dataQueue,common.cookie,thread_num)
    thread.start()
    thread_loaders.append(thread)