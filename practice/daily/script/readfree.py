import requests
import time
from bs4 import BeautifulSoup

# 登录验证地址
check_url = 'http://readfree.me/accounts/checkin'
# 准备cookie
cookie_str = "sessionid=fvkw046jeslicx5ku5ns5nd1wofkpv9i;csrftoken=K5cXO6TQ5QJU3rxS3u8p9KW6qMAtQj7iqS2LqMSarDmuOJANSxh9vIsJ9DzOsiCs; Hm_lvt_375aa6d601368176e50751c1c6bf0e82=1541646641,1542005925,1542072758,1542159932; Hm_lpvt_375aa6d601368176e50751c1c6bf0e82=%s"%(int(time.time()))
cookie = {}
for line in cookie_str.split(';'):
    name,value=line.strip().split('=',1)
    cookie[name]=value
# 使用cookie访问网站
res = requests.get(check_url,cookies=cookie)
file = open('D:\\Ayres\\readfree.csv', 'w', encoding="utf-8")
# 读取书籍列表
# for i in range(5070):
for i in range(10):
    print('Page %d:' % i)
    page_url = 'http://readfree.me/?page='+str(i+1)
    html = requests.get(page_url,cookies=cookie)
    bs_obj = BeautifulSoup(html.content,'html.parser')
    book_item_list = bs_obj.find_all('li','book-item')
    # print(bs_obj)
    # print(len(book_item_list))
    for item in book_item_list:
        book = {}
        book_info = item.find('div','book-info')
        aa = book_info.find('a','pjax')
        meta = item.find('div','book-meta muted')
        score = meta.find('span','badge badge-success').get_text()
        # print(aa)
        print('*********************************')
        book['href'] = aa.get('href')
        book['name'] = aa.get_text().strip()
        book['score'] = score
        file.write(aa.get('href')+','+aa.get_text().strip()+'\n')
        book_url = 'http://readfree.me'+aa.get('href')+'?_pjax=%23pjax'
        book_html = requests.get(book_url,cookies=cookie)
        book_obj = BeautifulSoup(book_html.content, 'html.parser')
        # print(book_obj)
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
        book['mobi'] = sorted(mobi,key=lambda x:x[1],reverse=True)
        book['pdf'] = sorted(pdf,key=lambda x:x[1],reverse=True)
        book['down'] = total_down_num
        print(book)

