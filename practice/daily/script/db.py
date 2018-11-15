import pymysql

def connect_readfree_db():
    return pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='222222',
                           database='readfree',
                           charset='utf8')

def select(book_link):
    conn = connect_readfree_db()
    cursor = conn.cursor()
    cursor.execute(("SELECT  * FROM book where book_link = \'%s\'") % book_link)
    row = cursor.rowcount
    result = cursor.fetchall()
    print(row)
    print(len(result))

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
        print(sql)
        print(params)
        cursor.execute(sql, params)
        conn.commit()
        cursor.close()
        return 1
    except Exception as e:
        print(e)
        return 0

original = {'href': '/book/6435891/', 'name': '飘', 'score': '9.8', 'douban': 'http://book.douban.com/subject/6435891', 'down': 97, 'most_mobi': '/edition/1514eb4ad5138b75db6384cd47e10073/down/%E9%A3%98%E7%BE%8E%E5%9B%BD%E7%8E%9B%E6%A0%BC%E4%B8%BD%E7%89%B9%E7%B1%B3%E5%88%87%E5%B0%94.%E8%8C%83%E7%BA%AF%E6%B5%B7%E5%A4%8F%E6%97%BB%E8%AF%91.%E9%95%BF%E6%B1%9F%E6%96%87%E8%89%BA%E5%87%BA%E7%89%88%E7%A4%BE.2011-6.mobi', 'mobi': [('/edition/1514eb4ad5138b75db6384cd47e10073/down/%E9%A3%98%E7%BE%8E%E5%9B%BD%E7%8E%9B%E6%A0%BC%E4%B8%BD%E7%89%B9%E7%B1%B3%E5%88%87%E5%B0%94.%E8%8C%83%E7%BA%AF%E6%B5%B7%E5%A4%8F%E6%97%BB%E8%AF%91.%E9%95%BF%E6%B1%9F%E6%96%87%E8%89%BA%E5%87%BA%E7%89%88%E7%A4%BE.2011-6.mobi', 74)], 'pdf': []}

data = {}
data['book_link'] = original['href']
data['name'] = original['name']
data['score'] = float(original['score'])
data['douban_link'] = original.get('douban','')
data['down'] = original['down']
data['mobi_most'] = original.get('most_mobi','')
data['pdf_most'] = original.get('most_pdf','')
data['mobi'] = str(original['mobi'])
data['pdf'] = str(original['pdf'])

select('/book/6435891/')
# insert_data('book',data)