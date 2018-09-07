from jira import JIRA
import time
from datetime import datetime
import sys

class JiraTool:
    def __init__(self):
        self.server = 'http://192.168.8.6:8080/'
        self.username = 'username'
        self.basic_auth = (self.username, 'password')
        self.jiraClient = None
        self.login()

    def login(self):
        self.jiraClient = JIRA(server=self.server, basic_auth=self.basic_auth)
        if self.jiraClient is not None:
            return True
        else:
            return False

    def worklogs(self, issue):
        return self.jiraClient.worklogs(issue)

    def addWorklog(self,worklog):
        return self.jiraClient.add_worklog(issue=worklog.issue, timeSpent=worklog.timeSpent, reduceBy=worklog.timeSpent,
                                              comment=worklog.comment, user=self.username)

class WorkLog:
    def __init__(self,issue,comment):
        self.issue = issue
        self.comment = comment
        self.timeSpent = '1d'

def worklog(tool,issue,comment):
    display = ''
    print('正在登记[%s]工时，内容为[%s]' % (issue, comment))
    today_worklog = WorkLog(issue, comment)
    result = tool.addWorklog(today_worklog)
    print('登记工时[%s]成功！' % result)
    display += '\n' + str(datetime.now())
    display += '\n正在登记[{0}]工时，内容为[{1}]'.format(issue, comment)
    display += '\n登记工时[{0}]成功！'.format(result)
    return display

def appendLogFile(display):
    f = open('C:\\Users\\CTSIG\\work.log', 'a')
    f.write(display)
    f.close()

def jiraWorklog(issue,comment):
    display = '\n'
    tool = JiraTool()
    logs = tool.worklogs(issue)
    lastlog = None
    if logs is not None and len(logs) != 0:
        lastlog = logs[-1]
    if lastlog:
        last_date = lastlog.created[0:10]
        current = datetime.now()
        if last_date == str(current)[0:10]:
            repeated_display = '今日[{0}]已登记过工时[{1}]'.format(last_date, lastlog.id)
            print(repeated_display)
            display += repeated_display
        else:
            display += worklog(tool,issue,comment)
    else:
        display += worklog(tool,issue,comment)
    appendLogFile(display)

def task():
    issue_id = 'GEARS-752'
    worklog_comment = '根据IDCMS数据库设计文档，继续建表 '
    from_sys_argvs = False
    if from_sys_argvs:
        issue_id = sys.argv[1]
        worklog_comment = sys.argv[2]
    jiraWorklog(issue_id,worklog_comment)

task()