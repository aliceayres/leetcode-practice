'''
oss统计脚本
'''
import xlrd
import os
import shutil

class Record:
    def __init__(self,row,type,name):
        self.raw = []
        for i in range(5):
            element = row[i]
            if i == 0:
                element = str(int(element))
            if i == 4 and element == '':
                element = row[5]
            if i == 4 and element == '未通过':
                element = '不通过'
            self.raw.append(element.replace('\n',''))
        self.raw.append(type)
        self.raw.append(name)

class Analysis:
    def __init__(self):
        self.cache = {}
        self.data = []

    def analysis(self):
        print(self.cache)
        for item in self.cache.items():
            dt = []
            dt.append(str(item[0]))
            dt.append(str(item[1][2]))
            dt.append(str(26 - item[1][2]))
            dt.append(str(item[1][3]))
            dt.append(str(24 - item[1][3]))
            dt.append(str('%.2f' % (item[1][2]/26 * 100)))
            dt.append(str('%.2f'% (item[1][3]/24* 100)))
            dt.append(str(item[1][2] + item[1][3]))
            dt.append(str(50 - (item[1][2] + item[1][3])))
            dt.append(str('%.2f'% ((item[1][2] + item[1][3]) / 50 * 100)))
            self.data.append(','.join(dt))
        self.tocsv()

    def tocsv(self):
        root = r'C:\Users\CTSIG\Desktop\评审总结呵呵呵'
        if not os.path.exists(root):
            os.makedirs(root)
        total_filename = 'tablesana.csv'
        file = open(root + '\\' + total_filename, 'w', encoding="utf-8")
        title = ['系统', '概要通过', '概要不通过','详细通过','详细不通过','概要通过率','详细通过率', '总通过', '总不通过', '总通过率']
        file.write(','.join(title) + '\n')
        for record in self.data:
            file.write(record+ '\n')
        file.close()

def tablesFromExcel(dir,filename,name,analysis=None):
    print(dir+filename)
    workbook = xlrd.open_workbook(dir+filename)
    all_sheets = workbook.sheet_names()
    type = {2:'概要设计',3:'详细设计'}
    all = []
    if analysis is not None:
        analysis.cache[name] = {2:0,3:0}
    for k in range(2,3):
        sheet = workbook.sheet_by_name(all_sheets[k])  # workbook.sheet_by_index(1)
        rows = sheet.nrows
        for i in range(1, rows):
            record = Record(sheet.row_values(i), type[k], name)
            all.append(record)
            if analysis is not None:
                if record.raw[4] == '通过':
                    analysis.cache[name][k] += 1
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

def prepare_files(from_dir,target):
    if not os.path.exists(target+'\\dbd'):
         os.makedirs(target+'\\dbd')
         os.makedirs(target+'\\ded')
    for filename in os.listdir(from_dir):
        db_path = os.path.join(from_dir, filename)+r'\04.设计\数据库结构设计'
        de_path = os.path.join(from_dir, filename)+r'\04.设计\详细设计说明书'
        if os.path.exists(db_path):
            for i in os.listdir(db_path):
                if i.find('.xlsx') > 0 and i.find('评审记录') > 0:
                    shutil.copy(db_path+'\\'+i,target+'\\dbd')
        if os.path.exists(de_path):
            for i in os.listdir(de_path) :
                if i.find('.xlsx') > 0 and i.find('评审记录') > 0:
                    shutil.copy(de_path+'\\'+i, target+'\\ded')

if __name__ == '__main__':
    original = r'C:\Users\CTSIG\新建文件夹\ctgnetoss'
    target = r'C:\Users\CTSIG\Desktop\评审总结呵呵呵'
    # prepare_files(original,target)
    de_dir = target+'\\db'
    de_files = []
    for files in os.walk(de_dir):
        for file in files[2]:
            de_files.append(file)
    ana = Analysis()
    for i in range(len(de_files)):
        name = de_files[i].replace('CTGNET-OSS ','').replace('CTG Net-OSS ','').replace('系统配套改造评审记录.xlsx','').replace('系统评审记录.xlsx','').replace('数据库评审记录.xlsx','')
        tablesFromExcel(de_dir+'\\',de_files[i],name,analysis=ana)
    # tablesToCsvFile()
    ana.analysis()

