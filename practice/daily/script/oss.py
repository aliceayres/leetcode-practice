'''
oss统计脚本
'''
import xlrd
import os

class Record:
    def __init__(self,row,type,name):
        self.raw = []
        for i in range(5):
            element = row[i]
            if i == 0:
                element = str(int(element))
            if i == 4 and element == '未通过':
                element = '不通过'
            self.raw.append(element.replace('\n',''))
        self.raw.append(type)
        self.raw.append(name)

def tablesFromExcel(dir,filename,name):
    workbook = xlrd.open_workbook(dir+filename)
    all_sheets = workbook.sheet_names()
    type = {2:'概要设计',3:'详细设计'}
    for k in range(2,4):
        sheet = workbook.sheet_by_name(all_sheets[k])  # workbook.sheet_by_index(1)
        rows = sheet.nrows
        for i in range(1, rows):
            record = Record(sheet.row_values(i), type[k], name)
            global all
            all.append(record)
    return all

def tablesToCsvFile():
    root = r'C:\Users\CTSIG\Desktop\评审总结呵呵呵'
    if not os.path.exists(root):
         os.makedirs(root)
    total_filename = 'tables.csv'
    file = open(root + '\\'+ total_filename, 'w', encoding="utf-8")
    global all
    print(all)
    title = ['序号','评审点','情况','建议','评审结果','类型','所属系统']
    file.write(','.join(title) + '\n')
    for record in all:
        print(','.join(record.raw))
        file.write(','.join(record.raw)+'\n')
    file.close()

if __name__ == '__main__':
    dir_name = r'C:\Users\CTSIG\Desktop\评审总结呵呵呵\hhh5'
    list = []
    for files in os.walk(dir_name):
        for file in files[2]:
            list.append(file)
    print(list)
    names = ['DCAE','运营门户','控制器','编排器','动态资源']
    global all
    all = []
    for i in range(len(list)):
        tablesFromExcel(dir_name+'\\',list[i],names[i])
    tablesToCsvFile()

