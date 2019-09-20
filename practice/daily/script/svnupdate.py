# -*- coding: utf-8 -*-
import time
import os
import sys

def svnupdate(path):
    cmd = 'TortoiseProc.exe /command:update /path:"{}" /closeonend:0'.format(path)
    return os.system(cmd)

path = 'D:\Workhome\ctgnet oss'
svnupdate(path)
