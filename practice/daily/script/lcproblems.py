import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import ssl
class Solution:

    def __init__(self):
        self. cookieContent = "__cfduid=d5a9719e853c605eadac234eca17057041561948828; _ga=GA1.2.1612334839.1561948833; _gid=GA1.2.80402639.1570851105; csrftoken=aefhDfZV3p7NhBQ2Z0COtyoKEkppS2ms6KwBUnNMHsXd5DNPcsNL8IyrvPNRIMVv; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjU0NzU0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZmEwM2E4ZGZhNGIyOGU0ODhlYzZkZjZlYjY3NDcwYzg3OWU0NzQwOSIsImlkIjoyNTQ3NTQsImVtYWlsIjoiYWxpY2VheXJlc0BxcS5jb20iLCJ1c2VybmFtZSI6ImFuZ2VsZW5leWUiLCJ1c2VyX3NsdWciOiJhbmdlbGVuZXllIiwiYXZhdGFyIjoiaHR0cHM6Ly93d3cuZ3JhdmF0YXIuY29tL2F2YXRhci9lMTZjNmU0MDQyMzA3NzYwOTJmNTM1Y2E4MzliZGFkZi5wbmc_cz0yMDAiLCJ0aW1lc3RhbXAiOiIyMDE5LTEwLTEyIDAzOjM0OjAzLjY2NDU4NCswMDowMCIsIklQIjoiMjIyLjEyOC40MS4xNjUiLCJJREVOVElUWSI6IjAxZmU2ZDk2ZjUxMmRmMTVjYzFiMTAzNDVkNmIzN2Q5IiwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.rf0WtfxBYV0Ak8iTOLKwpzF72SbWCEFkySLCUdhrpHQ; __stripe_mid=a10673e2-eefb-41c5-9a6f-b423f2c49b8c; c_a_u=\"YW5nZWxlbmV5ZQ==:1iJAfR:2bvm-B_VSroFdzmNDbH3JsK3RGQ\"; _gat=1"
        self.cookie = {}
        for line in self.cookieContent.split(';'):
            name, value = line.strip().split('=', 1)
            self.cookie[name] = value
        ssl._create_default_https_context = ssl._create_unverified_context
        self.headers = {}
        self.headers['content-type'] = 'application/json'
        self.headers['user-agent']="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        self.headers['x-csrftoken'] = "aefhDfZV3p7NhBQ2Z0COtyoKEkppS2ms6KwBUnNMHsXd5DNPcsNL8IyrvPNRIMVv"
        self.headers['x-newrelic'] = "UAQDVFVRGwEAXVlbBAg="

    def solute(self):
        return

    def doGet(self,url,isJson):
        resp = requests.get(url)
        print(resp)
        if resp.status_code == 200:
            if isJson is True:
                return json.loads(resp.text)
            else:
                return resp
        return None


    def doPost(self,url,parameter):
        ssl._create_default_https_context = ssl._create_unverified_context
        resp = requests.post(url,data=parameter,cookies=self.cookie,headers=self.headers,verify=True)
        print(resp.content)
        if resp.status_code == 200:
            return json.loads(resp.text)
        return resp


if __name__ == '__main__':
    slt = Solution()
    # # get all problems list
    # all_url = "https://leetcode.com/api/problems/all/"
    # result = slt.doGet(all_url,True)
    # pairs = result['stat_status_pairs']
    # print(len(pairs))
    # print(result['stat_status_pairs'])
    # for p in pairs:
    #     print(p)
    # # get specific problem data
    #
    # response = slt.doGet(problem_url,False)
    # print(response)
    # '''
    # graphql = "https://leetcode.com/graphql"
    # parameter =  {"operationName": "questionData",
    #               "variables": {"titleSlug": "longest-substring-without-repeating-characters"},
    #               "csrf_token": "aefhDfZV3p7NhBQ2Z0COtyoKEkppS2ms6KwBUnNMHsXd5DNPcsNL8IyrvPNRIMVv",
    #  "query": "query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"}
    # problem = slt.doPost(graphql,parameter)
    # print(problem)
    # '''
    problem_url = "https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/"
    driver = webdriver.Chrome("D:\Ayres\download\chromedriver_win32\chromedriver.exe")
    driver.get(problem_url)
    driver.implicitly_wait(660)
    title = driver.find_elements_by_xpath("//title/*")
    for t in title:
        print(t.text)
    div = driver.find_elements_by_xpath("//meta[@name='description']")
    for e in div:
        print(e.get_attribute("content"))
    driver.close()




