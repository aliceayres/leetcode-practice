from jira import JIRA
import time
from datetime import datetime
import configparser
import json
import sys

class WorkLog:
    def __init__(self,issue,comment):
        self.issue = issue
        self.comment = comment
        self.timeSpent = '1d'

class JiraTool:
    def __init__(self):
        self.config_filename = r'/Users/ayres/home/u/wtf/config.ini'
        self.config = self.readFromConfig()
        self.basic_auth = (self.config['username'], self.config['password'])
        self.jiraClient = None
        self.login()

    def login(self):
        self.jiraClient = JIRA(server=self.config['server'], basic_auth=self.basic_auth)
        if self.jiraClient is not None:
            return True
        else:
            return False

    def readFromConfig(self):
        conf = configparser.RawConfigParser()
        # conf = configparser.ConfigParser()
        conf.read(self.config_filename, encoding='UTF-8')
        config = {}
        config['server'] = conf.get("jira", "server")
        config['automode'] = conf.get("worklog", "automode")
        config['project'] = conf.get("worklog", "project")
        config['issue'] = conf.get("worklog", "issue")
        config['log'] = conf.get("worklog", "log")
        config['username'] = conf.get("jira", "username")
        config['password'] = conf.get("jira", "password")
        config['allowrepeat'] = conf.get("worklog", "allowrepeat")
        return config

    def worklogs(self, issue):
        return self.jiraClient.worklogs(issue)

    def addWorklog(self,worklog):
        return self.jiraClient.add_worklog(issue=worklog.issue, timeSpent=worklog.timeSpent, reduceBy=worklog.timeSpent,
                                              comment=worklog.comment, user=self.config['username'])

    def projects(self):
        # <JIRA Project: key='APM', name='验收项目管理', id='11900'>
        return self.jiraClient.projects()

    def issues(self):
        rt = self.jiraClient.search_issues('project = APM AND assignee in (currentuser())',json_result=True)
        # print(json.dumps(rt, ensure_ascii=False))
        return rt['issues']

    def inPeriod(self,begin,end):
        today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        t = time.strptime(today, '%Y-%m-%d')
        t1 = time.strptime(begin, '%Y-%m-%d')
        t2 = time.strptime(end, '%Y-%m-%d')
        return t1 <= t <= t2

    def isEnd(self,end):
        today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        t = time.strptime(today, '%Y-%m-%d')
        t2 = time.strptime(end, '%Y-%m-%d')
        return t >= t2

    def updateIssueStatus(self,issue,transition):
        self.jiraClient.transition_issue(issue,transition=transition)

    def uniqueIssue(self,project):
        rt = self.jiraClient.search_issues('project = '+ project +' AND assignee in (currentuser())',json_result=True)
        issues = rt['issues']
        for map in issues:
            if map['fields']['issuetype']['subtask'] is not True:
                continue
            begin = map['fields']['customfield_10420']
            end = map['fields']['customfield_10421']
            if self.inPeriod(begin,end) is not True:
                continue
            issuee = {}
            issuee['key'] = map['key']
            issuee['summary'] = map['fields']['summary']
            # print(map['key'])
            # print(map['fields']['summary'])
            # print(map['fields']['status']['name'])
            # print(map['fields']['status']['id'])
            # print(map['fields']['status']['statusCategory'])
            # print(map['fields']['duedate'])
            # print(map['fields']['customfield_10420'])
            # print(map['fields']['customfield_10421'])
            issue = self.jiraClient.issue(map['key'])
            transitions = self.jiraClient.transitions(issue)
            for t in transitions:
                print(t)
            if map['fields']['status']['name'] == '待办':
                # 更新处理中
                self.updateIssueStatus(map['key'],11)
            if self.isEnd(end) is True:
                # 更新完成
                self.updateIssueStatus(map['key'],21)
            return issuee
        return None

    def worklog(self,issue,comment):
        display = ''
        print('正在登记[%s]工时，内容为[%s]' % (issue, comment))
        today_worklog = WorkLog(issue, comment)
        result = self.addWorklog(today_worklog)
        print('登记工时[%s]成功！' % result)
        display += '\n' + str(datetime.now())
        display += '\n正在登记[{0}]工时，内容为[{1}]'.format(issue, comment)
        display += '\n登记工时[{0}]成功！'.format(result)
        return display

    def dailyLog(self):
        uni = self.uniqueIssue(self.config['project'])
        if self.config['automode'] == 'True':
            if uni is not None:
                print(uni)
                self.oldLog(uni['key'],uni['summary']+' '+self.config['log'])
            else:
                self.oldLog(self.config['issue'], self.config['log'])
        else:
            self.oldLog(self.config['issue'], self.config['log'])

    def oldLog(self,issue, comment):
        display = '\n'
        logs = self.worklogs(issue)
        lastlog = None
        if logs is not None and len(logs) != 0:
            lastlog = logs[-1]
        if lastlog:
            last_date = lastlog.created[0:10]
            current = datetime.now()
            if self.config['allowrepeat'] == 'True':
                display += self.worklog(issue, comment)
            else:
                if last_date == str(current)[0:10]:
                    repeated_display = '今日[{0}]已登记过工时[{1}]'.format(last_date, lastlog.id)
                    print(repeated_display)
                    display += repeated_display
                else:
                    display += self.worklog(issue, comment)
        else:
            display += self.worklog(issue, comment)
        self.appendLogFile(display)

    def appendLogFile(self,display):
        f = open('/Users/ayres/home/u/wtf/work.log', 'a')
        f.write(display)
        f.close()

def daily():
    tool = JiraTool()
    tool.dailyLog()

# def task():
#     issue_id = 'GEARS-752'
#     worklog_comment = '根据IDCMS数据库设计文档，继续建表 '
#     from_sys_argvs = False # True
#     if from_sys_argvs:
#         issue_id = sys.argv[1]
#         worklog_comment = sys.argv[2]
#     tool = JiraTool()
#     tool.oldLog(issue_id,worklog_comment)

daily()
