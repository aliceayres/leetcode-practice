#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
import logging

LOG_FORMAT = '%(asctime)s - %(filename)s[L%(lineno)d] - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

def mkSubFile(lines, filename,head, sub):
    root = 'D:\\Ayres\\sql\\'
    # [des_filename, extname] = os.path.splitext(srcName)
    print('make file: %s' % filename)
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
        for line in fin:
            buf.append(line)
            if line.find('-- Table structure for') > -1:
                last_header_line.append(line)
                idx = line.index('-- Table structure for ')
                current_table = line[idx+len('-- Table structure for '):-1]
                print(current_table)
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
    finally:
        fin.close()


if __name__ == '__main__':
    begin = time.time()
    splitByHeaderLine('D:\\Ayres\\idc.sql', '-- ----------------------------\n')
    end = time.time()
    print('time is %d seconds ' % (end - begin))
    fields_set = []
    for (root, dirs, files) in os.walk("D:\\Ayres\\sql\\"):
        for filename in files:
            sql_file = os.path.join(root, filename)
            print(sql_file)
            fin = open(sql_file, 'r', encoding="utf-8")
            lines = fin.readlines()
            fields_buf = []
            comments_buf = []
            f_begined = False
            c_begined = False
            for ln in lines:
                ln = ln.replace('"', '')
                ln = ln.replace('IDC.','')
                ln = ln.replace(' BYTE)', ')')
                # change drop
                if ln.find('DROP TABLE ')>-1:
                    array = ln.split(' ')
                    array[1] = 'TABLE IF EXISTS'
                    ln = ' '.join(array)
                    #print(ln)
                if ln.find('CREATE TABLE ')>-1:
                    f_begined = True
                if f_begined and ln == ')\n':
                    f_begined = False
                if f_begined and ln != ')\n' and ln.find('CREATE TABLE ')== -1:
                    print(ln)
                    array = ln.split(' ')
                    fields_set.append(array[1])
        sets = sorted(set(fields_set))
        print('all datatype %d below:' % len(sets))
        for st in sets:
            print(st)

