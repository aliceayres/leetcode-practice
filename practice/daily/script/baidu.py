# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.ttk import *
import sqlite3

def write_file(file_dict, f, item, gap=""):
    if item == "/":
        # f.write("━" + "/" + "\n")
        for i in file_dict["/"]:
            # f.write("┣" + "━" + i + "\n")
            i = item + i + "/"
            print(i)
            f.write(i + "\n")
            if i in file_dict:
                write_file(file_dict, f, i, gap="┣━")
    else:
        gap = "┃  " + gap
        for i in file_dict[item]:
            # f.write(gap + i + "\n")
            i = item + i + "/"
            print(i)
            f.write(i+"\n")
            if i in file_dict:
                write_file(file_dict, f, i, gap)

def create_baiduyun_filelist():
    db = "C:/Users/CTSIG/AppData/Roaming/baidu/BaiduNetdisk/users/1ce0348b5c9145c78bc0fd68c43cf214/BaiduYunCacheFileV0.db"
    f = "C:/Users/CTSIG/Desktop/menu.txt"
    file_dict = {}
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("select * from cache_file")
    while True:
        value = cursor.fetchone()
        if not value:
            break
        path = value[2]
        name = value[3]
        size = value[4]
        isdir = value[6]
        if path not in file_dict:
            file_dict[path] = []
            file_dict[path].append(name)
        else:
            file_dict[path].append(name)
     # for item in file_dict:
     #     print(item)
    with open(f, "w", encoding='utf-8') as fp:
        write_file(file_dict, fp, "/")

create_baiduyun_filelist()