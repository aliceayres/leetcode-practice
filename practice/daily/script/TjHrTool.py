# -*- coding:utf-8 -*-
import json
import requests
import threading

class Solution:

    def doPost(self,url,parameter):
        resp = requests.post(url, data=parameter)
        print(resp)
        if resp.status_code == 200:
            return json.loads(resp.text)
        return None

    def action(self):
        insert_realname = '姓名'
        insert_phone = '18600000000'
        insert_documentNo = '200200190000000000'
        insert_subDate = '2018-05-31'
        insert_address = '天津人力资源发展促进中心'
        insert_isMorning = 1
        parameter = {
            'realname': insert_realname,
            'phone': insert_phone,
            'documentNo': insert_documentNo,
            'subDate': insert_subDate,
            'address': insert_address,
            'isMoring': insert_isMorning
        }
        print('sub thread start!the thread name is:%s\r' % threading.currentThread().getName())
        self.task(parameter)

    def task(self,parameter):
        while True:
            if slt.submit(parameter):
                break

    def submit(self,parameter):
        default_root = 'http://yy.ihrdata.com'
        submit_api = '/subscribe/insert.json'
        url = default_root + submit_api
        # result = self.doPost(url,parameter)
        # if result != None :
        #     print(result)
        #     print(result['success'])
        #     print(result['message'])
        #     print(result['status'])
        #     return result['success']
        # else:
        #     print('Failed to request.')
        #     return False

slt = Solution()
for i in range(4):
    th = threading.start_new_thread(target=slt.action(), args=(i,))
    th.start()


