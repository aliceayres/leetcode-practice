from jira import JIRA
import sys

class JiraTool:
    def __init__(self):
        self.server = 'http://192.168.8.6:8080/'
        self.basic_auth = ('username', 'password')
        self.jiraClient = None
        self.login()

    def login(self):
        self.jiraClient = JIRA(server=self.server, basic_auth=self.basic_auth)
        if self.jiraClient is not None:
            return True
        else:
            return False

    def client(self):
        return self.jiraClient

class WorkLog:
    def __init__(self,issue,comment):
        self.issue = issue
        self.comment = comment
        self.timeSpent = '1d'
        self.timeSpentSeconds = 28800
        self.user = 'username'
        self.tool = JiraTool()

    def addWorkLog(self):
        return self.tool.client().add_worklog(issue=self.issue, timeSpent=self.timeSpent,reduceBy=self.timeSpent,comment=self.comment, user=self.user)


# issue_id = sys.argv[1]
# worklog_comment = sys.argv[2]
issue_id = 'GEARS-752'
worklog_comment = '登记工作'
print('正在登记[%s]工时，内容为[%s]' % (issue_id,worklog_comment))
today_worklog = WorkLog(issue_id,worklog_comment)
result = today_worklog.addWorkLog()
print('登记工时[%s]成功！' % result)