#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
import logging
import xlrd
import cx_Oracle
from datetime import *

class OracleHelper:
    def __init__(self):
        self.charset='utf8'
        try:
            self.conn = cx_Oracle.connect('scott/tiger@DESKTOP-IASSOVJ/orcl')
            self.cur=self.conn.cursor()
        except cx_Oracle.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def selectDb(self,db):
      try:
          self.conn.select_db(db)
      except cx_Oracle.Error as e:
          print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def query(self,sql):
        try:
           n=self.cur.execute(sql)
           return n
        except cx_Oracle.Error as e:
           print("Mysql Error:%s\nSQL:%s" %(e,sql))
           raise e


    def queryRow(self,sql):
        self.query(sql)
        result = self.cur.fetchone()
        return result

    def queryAll(self,sql):
        self.query(sql)
        result=self.cur.fetchall()
        desc =self.cur.description
        d = []
        for inv in result:
             _d = {}
             for i in range(0,len(inv)):
                 _d[desc[i][0]] = str(inv[i])
             d.append(_d)
        return d

    def insert(self,p_table_name,p_data):
        for key in p_data:
            if (isinstance(p_data[key],str) or isinstance(p_data[key],datetime) ):
                if str(p_data[key])=="None":
                    p_data[key]='null'
                else:
                    p_data[key] = "'"+str(p_data[key]).replace('%','％').replace('\'','')+"'"
            else:
                p_data[key] = str(p_data[key])

        key   = ','.join(p_data.keys())
        value = ','.join(p_data.values())
        real_sql = "INSERT INTO " + p_table_name + " (" + key + ") VALUES (" + value + ")"
        return self.query(real_sql)
    def getLastInsertId(self):
        return self.cur.lastrowid

    def rowcount(self):
        return self.cur.rowcount

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

LOG_FORMAT = '%(asctime)s - %(filename)s[L%(lineno)d] - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Oracle获取用户所有表：select count(*) from user_tables

def mkSubFile(lines, filename,head, sub):
    root = 'D:\\Ayres\\sqls\\'
    # [des_filename, extname] = os.path.splitext(srcName)
    # print('make file: %s' % filename)
    fout = open(root+filename, 'w',encoding="utf-8")
    try:
        fout.writelines([head])
        fout.writelines(lines)
        return sub + 1
    finally:
        fout.close()

def splitByHeaderLine(filename, header_line):
    fin = open(filename, 'r', encoding="utf-8")
    try:
        head = fin.readline()
        buf = []
        sub = 1
        last_header_line = []
        current_table = None
        all_table = ''
        alls = []
        for line in fin:
            buf.append(line)
            if line.find('-- Table structure for') > -1:
                last_header_line.append(line)
                idx = line.index('-- Table structure for ')
                current_table = line[idx+len('-- Table structure for '):-1]
                all_table += current_table+'\n'
                alls.append(current_table)
                # print(current_table)
            if line == header_line:
                last_header_line.append(line)
            if current_table is not None and len(last_header_line) == 3:
                src_name = str(sub)+' '+current_table+'.sql'
                sub = mkSubFile(buf[:-1], src_name, head, sub)
                current_table = None
                last_header_line = []
                buf = []
        if len(buf) != 0:
            src_name = str(sub) + ' ' + current_table + '.sql'
            sub = mkSubFile(buf, src_name, head, sub)
        # list all table to file
        file = open('D:\\Ayres\\idc_oracle.csv', 'w', encoding="utf-8")
        file.write(all_table)
        file.close()
    finally:
        fin.close()
    return alls

def transDatatype(line):
    array = line.split(' ')
    datatype = array[1]
    if line.find('BFILE') > -1 or array[1].find('RAW(18)') > -1 or array[1].find('UROWID(4000)') > -1:
        array[1] = array[1].replace('BFILE','BLOB')
        array[1] = array[1].replace('RAW(18)', 'BLOB')
        array[1] = array[1].replace('UROWID(4000)', 'BLOB')
    if array[1].find('LONG') > -1 or array[1].find('CLOB') > -1 or array[1].find('NCLOB') > -1:
        array[1] = array[1].replace('LONG', 'TEXT')
        array[1] = array[1].replace('NCLOB', 'TEXT')
        array[1] = array[1].replace('CLOB', 'TEXT')
    if array[1].find('ROWID') > -1:
        array[1] = array[1].replace('ROWID', 'BIGINT')
    if array[1].find('DATE') > -1:
        array[1] = array[1].replace('DATE', 'DATETIME')
    if array[1].find('FLOAT(126)') > -1:
        array[1] = array[1].replace('FLOAT(126)', 'FLOAT(8)')
    if array[1].find('NCHAR') > -1:
        array[1] = array[1].replace('NCHAR', 'VARCHAR')
    if array[1].find('NVARCHAR2') > -1:
        array[1] = array[1].replace('NVARCHAR2', 'VARCHAR')
    if array[1].find('VARCHAR2') > -1:
        array[1] = array[1].replace('VARCHAR2', 'VARCHAR')
    if array[1].find('VARCHAR(') > -1:
        vv = array[1].split('(')
        vl = int(vv[1][:-1])
        if vl >= 300:
            array[1] = 'TEXT'
    if datatype == 'NUMBER':
        array[1] = array[1].replace('NUMBER', 'INT')
    if datatype.find('NUMBER(') > -1:
        if datatype.find(',') > -1:
            array[1] = array[1].replace('NUMBER', 'NUMERIC')
        else:
            nn = datatype.split('(')
            length = int(nn[1][:-1])
            if length <= 8:
                array[1] = array[1].replace('NUMBER', 'INT')
            else:
                array[1] = array[1].replace('NUMBER', 'BIGINT')
    if array[1].find('NUMERIC(1,2)') > -1:
        array[1] = array[1].replace('NUMERIC(1,2)', 'NUMERIC(2,2)')
    ll = ' '.join(array)
    if ll.find('TEXT RAW') > -1:
        ll = ll.replace('TEXT RAW', 'BLOB')
    if ll.find('LONG RAW') > -1:
        ll = ll.replace('LONG RAW', 'BLOB')
    return ll

def runStructure():
    splitByHeaderLine( "D:\\Ayres\\structure.sql", '-- ----------------------------\n')
    fields_set = []
    to_root = "D:\\Ayres\\oracle_idcms\\"
    to_filename = "D:\\Ayres\\all.sql"
    all_sql = []
    for (root, dirs, files) in os.walk("D:\\Ayres\\sqls\\"):
        for filename in files:
            sql_file = os.path.join(root, filename)
            # print(sql_file)
            fin = open(sql_file, 'r', encoding="utf-8")
            lines = fin.readlines()
            fields_buf = []
            comments_buf = []
            f_begined = False
            c_begined = False
            new_lines = []
            comment_dict = {}
            table_comment = ''
            table_name = ''
            for ln in lines:
                ln = ln.replace('"', '')
                ln = ln.replace('IDC.', '')
                ln = ln.replace(' BYTE)', ')')
                ln = ln.replace('DEFAULT SYSDATETIME','')
                if ln.find('COMMENT ON TABLE ') > -1:
                    array = ln.split(' ')
                    table_comment = array[-1][:-2]
                if ln.find('COMMENT ON COLUMN ') > -1:
                    array = ln.split(' IS ')
                    cmt = array[-1][:-2]
                    ffarray = ln.split(' ')
                    fstr = ffarray[3]
                    farray = fstr.split('.')
                    comment_dict[farray[-1]] = cmt.replace('\'','')
                if ln.find('-- Table structure for ') > -1:
                    table_name = ln.split(' ')[-1][:-1]
            # print(comment_dict)
            for ln in lines:
                ln = ln.replace('"', '')
                ln = ln.replace('IDC.','')
                ln = ln.replace(' BYTE)', ')')
                ln = ln.replace('DEFAULT SYSDATETIME', '')
                if ln.find('-- ') > -1 and ln.find('COMMENT ON COLUMN ') == -1:
                    new_lines.append(ln)
                if ln == ';\n':
                    new_lines.append(ln)
                # change drop
                if ln.find('DROP TABLE ')>-1:
                    array = ln.split(' ')
                    array[1] = 'TABLE IF EXISTS'
                    ln = ' '.join(array)
                    new_lines.append(ln)
                    #print(ln)
                if ln.find('CREATE TABLE ')>-1:
                    new_lines.append(ln)
                    f_begined = True
                if f_begined and ln == ')\n':
                    f_begined = False
                    if table_comment != '':
                        table_comment = table_comment.replace('\'','')
                        ln = ')COMMENT = \'' + table_comment + '\'\n'
                    new_lines.append(ln)
                if f_begined and ln != ')\n' and ln.find('CREATE TABLE ') == -1:
                    array = ln.split(' ')
                    lnn = transDatatype(ln)
                    fields_set.append(array[1])
                    lnn = lnn.replace('--????', '')
                    lnn = lnn.replace('?', '')
                    lnn = lnn.replace('VARCHAR(32 CHAR)', 'VARCHAR(32)')
                    lnn = lnn.replace('DEFAULT sys_guid()', '')
                    lnn = lnn.replace('DEFAULT (\'N\')', 'DEFAULT \'N\'')
                    lnn = lnn.replace('DEFAULT (\'Y\')', 'DEFAULT \'Y\'')
                    lnn = lnn.replace('DEFAULT (\'1\')', 'DEFAULT \'1\'')
                    lnn = lnn.replace('DEFAULT ((0))', 'DEFAULT 0')
                    lnn = lnn.replace('DEFAULT SYSDATETIME', '')
                    lnn = lnn.replace('DEFAULT sysdate', '')
                    lnn = lnn.replace('DEFAULT SYSDATE', '')
                    lnn = lnn.replace('DEFAULT (sysdate)', '')
                    lnn = lnn.replace('DEFAULT to_date(\'1900-1-1\',\'YYYY-MM-DD\')', '')
                    lnn = lnn.replace('DEFAULT to_date(\'2999-01-01 00:00:00\',\'YYYY-MM-DD HH24:MI:SS\')', '')
                    if comment_dict.get(array[0]) is not None:
                        field_comment = comment_dict.get(array[0])
                        if lnn[-2] == ',':
                            lnn = lnn[:-2]
                            lnn += ' COMMENT \'' + field_comment + '\',\n'
                        else:
                            lnn = lnn[:-1]
                            lnn += ' COMMENT \'' + field_comment + '\'\n'
                    if array[0] == 'RANGE':
                        lnn = lnn.replace('RANGE', 'RANGES')
                    if array[0] == 'KEY':
                        lnn = lnn.replace('KEY', 'KEYES')
                    if array[0] == 'MAXVALUE':
                        lnn = lnn.replace('MAXVALUE', 'MAXVALUES')
                    if array[0] == 'CHARACTER':
                        lnn = lnn.replace('CHARACTER', 'CHARACTERS')
                    if array[0] == 'RESTRICT':
                        lnn = lnn.replace('RESTRICT', 'RESTRICTS')
                    if array[0] == 'CODE':
                        lnn = lnn.replace('CODE', 'CODES')
                    if array[0] == 'SQL':
                        lnn = lnn.replace('SQL', 'SQLS')
                    if array[0] == 'CONDITION':
                        lnn = lnn.replace('CONDITION', 'CONDITIONS')
                    if array[0] == 'PRECISION':
                        lnn = lnn.replace('PRECISION', 'PRECISIONS')
                    if array[0] == 'STATUS':
                        lnn = lnn.replace('STATUS', 'STATUSES')
                    if array[0] == 'RECORDSN' and table_name == 'IDC_PROC':
                        lnn = lnn.replace('DEFAULT \'\'', '')
                    new_lines.append(lnn)
            #for nln in new_lines:
                #print(nln)
            file = open(to_root+table_name+'.sql', 'w', encoding="utf-8")
            file.write(''.join(new_lines))
            all_sql.append(''.join(new_lines))
            file.close()
        file = open(to_filename, 'w', encoding="utf-8")
        file.write(''.join(all_sql))
        file.close()
        # sets = sorted(set(fields_set))
        # print('all datatype %d below:' % len(sets))
        # for st in sets:
        #     print(st)

def runDataset():
    return

def getDesignTableDict():
    workbook = xlrd.open_workbook('D:\\Ayres\\design.xlsx')
    all_sheets = workbook.sheet_names()
    sheet = workbook.sheet_by_name(all_sheets[0])  # workbook.sheet_by_index(1)
    rows = sheet.nrows
    design_tables = {}
    for j in range(1, rows):
        tb = sheet.row_values(j)[0]
        design_tables.setdefault(tb.upper(), 1)
    return design_tables

def getIdcAllTablesList():
    workbook = xlrd.open_workbook('D:\\Ayres\\oracle_info.xlsx')
    all_sheets = workbook.sheet_names()
    sheet = workbook.sheet_by_name(all_sheets[0])  # workbook.sheet_by_index(1)
    rows = sheet.nrows
    all_tables = []
    for j in range(1, rows):
        tb = sheet.row_values(j)[0]
        if tb == '':
            break
        num = int(sheet.row_values(j)[1])
        print((tb,num))
        all_tables.append((tb,num))
    return all_tables

def runAllCompare():
    compare_tables = '序号,表名,记录数,设计是否存在,是否补充,不补充原因\n'
    design_tables = getDesignTableDict()
    all_tables = getIdcAllTablesList()
    print(all_tables)
    count = 0
    for tt in all_tables:
        ele = []
        count += 1
        ele.append(str(count))
        ele.append(tt[0])
        ele.append(str(tt[1]))
        if design_tables.get(tt[0], None) is not None:
            ele.append('Y')
        else:
            ele.append('')
        print(','.join(ele) + ',,\n')
        compare_tables += ','.join(ele) + '\n'
        # print('count: %d ' % count)
        #  print('design: %d ' % len(design_tables))
    file = open('D:\\Ayres\\idc全部表统计信息.csv', 'w', encoding="utf-8")
    file.write(compare_tables)
    file.close()
    # print(all_tables)
    # print(design_tables)

def runCompare():
    all_tables = splitByHeaderLine('D:\\Ayres\\idc.sql', '-- ----------------------------\n')
    compare_tables = '序号,表名,设计是否存在,记录数量,是否补充,不补充原因\n'
    workbook = xlrd.open_workbook('D:\\Ayres\\design.xlsx')
    all_sheets = workbook.sheet_names()
    sheet = workbook.sheet_by_name(all_sheets[0])  # workbook.sheet_by_index(1)
    rows = sheet.nrows
    design_tables = {}
    for j in range(1, rows):
        tb = sheet.row_values(j)[0]
        design_tables.setdefault(tb.upper(), 1)
    # print(all_tables)
    # print(design_tables)
    workbook_row = xlrd.open_workbook('D:\\Ayres\\rows.xlsx')
    all_sheets_row = workbook_row.sheet_names()
    sheet_row = workbook_row.sheet_by_name(all_sheets_row[0])  # workbook.sheet_by_index(1)
    rowss = sheet_row.nrows
    rows_tables = {}
    for j in range(0, rowss):
        tb = sheet_row.row_values(j)[0]
        rows_tables.setdefault(tb.upper(), sheet_row.row_values(j)[1])
    # print(all_tables)
    # print(design_tables)
    count = 0
    for tt in all_tables:
        ele = []
        count += 1
        ele.append(str(count))
        ele.append(tt)
        if design_tables.get(tt, None) is not None:
            ele.append('Y')
        else:
            ele.append('')
        if rows_tables.get(tt, None) is not None:
            ele.append(str(rows_tables.get(tt, None)))
        print(','.join(ele) + ',,\n')
        compare_tables += ','.join(ele) + '\n'
        # print('count: %d ' % count)
        #  print('design: %d ' % len(design_tables))
    file = open('D:\\Ayres\\oracle数据统计信息.csv', 'w', encoding="utf-8")
    file.write(compare_tables)
    file.close()

if __name__ == '__main__':
    runStructure()
    # runDataset()
    # runAllCompare()

