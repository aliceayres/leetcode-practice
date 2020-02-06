import logging
import configparser
import pandas as pd
from sqlalchemy import create_engine

LOG_FORMAT = '%(asctime)s - Thread[%(thread)s] - %(filename)s[L%(lineno)d] - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

class Tool:
    def __init__(self):
        self.config_filename = 'transdb.ini'
        logging.info("@@@@ initialize import db config...")
        self.conf = configparser.ConfigParser()
        self.conf.read(self.config_filename, encoding='UTF-8')
        # mysql
        self.host = self.conf.get("mysql", "host")
        self.port = self.conf.getint("mysql", "port")
        self.username = self.conf.get("mysql", "username")
        self.password = self.conf.get("mysql", "password")
        self.database = self.conf.get("mysql", "database")
        self.charset = self.conf.get("mysql", "charset")

    def get_connect(self):
        url = format('mysql+mysqlconnector://%s:%s@%s:%s/%s?charset=%s'
                     % (self.username,self.password,self.host,str(self.port),self.database,self.charset))
        engine = create_engine(url, echo=False)
        return engine

    def run(self):
        filename = self.conf.get("config", "filename")
        table = self.conf.get("config", "table")
        df = pd.read_csv(filename, encoding='utf8')
        # fields = list(df.columns)
        # print(df.T.to_dict())
        conn = self.get_connect()
        df.to_sql(name=table, con=conn, if_exists='append', index=False)

if __name__ == '__main__':
    tool = Tool()
    tool.run()