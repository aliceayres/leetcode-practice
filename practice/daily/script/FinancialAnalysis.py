# -*- coding:utf-8 -*-

from urllib import request
import os
import pandas as pd
import numpy as np
import chardet
import tushare as ts

class env:
    analysis_mode = True
    basic_mode = True
    refresh_download = True
    load_before_analysis = True
    is_linux = False
    stocks = ['002304']  # '000333','000651', '600166', '002508','000423','000541'
    report_have = 3
    year_have = 5

class seperator:
    linux = "/"
    windows = "/"

class profile:
    linux_root = '/Users/ayres/home/quotes'
    windows_root = 'D:/Ayres/finance'

    summary_dir = 'summary'
    stock_dir = 'stock'
    config_dir = 'config'

    config_filename = "config.csv"
    summary_suffix = "_financial_summary.csv"
    year_suffix = "_financial_year_summary.csv"
    final_suffix = "_financial_final.csv"
    basic_filename = 'basic.csv'

    csv = '.csv'
    file = {'primary':'_primary_finance',
            'abstract':'_finance_abstract',
            'balance':'_balance_sheet',
            'income': '_income_statement',
            'cashflow': '_cashflow_statement',
            'earning': '_earning_power',
            'repaying': '_repaying_power',
            'growth': '_growth',
            'operation': '_operation'
            }

class config:
    service = 'http://quotes.money.163.com/service/'

    prefix = {'primary': 'zycwzb_',
              'abstract': 'cwbbzy_',
              'balance': 'zcfzb_',
              'income': 'lrb_',
              'cashflow': 'xjllb_'
              }
    # type=year
    suffix = {'report': '.html?type=report',
              'earning': '.html?type=report&part=ylnl',
              'repaying': '.html?type=report&part=chnl',
              'growth': '.html?type=report&part=cznl',
              'operation': '.html?type=report&part=yynl',
              'html':'.html'
                    }

class indexs:
    asset = 94
    lability = 136
    income = 20
    profit = 23
    cash = 42

class fd:
    type = 0
    index = 1
    name = 2
    data = 3

def save_file(url, lpth):
    with request.urlopen(url) as web:
        with open(lpth, 'wb') as outfile:
            outfile.write(web.read())

def mkdir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def root():
    root = profile.windows_root
    if env.is_linux:
        root = profile.linux_root
    return root

def absolute_path(path):
    sep = seperator.windows
    if env.is_linux:
        sep = seperator.linux
    join = root()
    for i in range(0,len(path)):
        join += '' + sep + path[i]
    return join

def get_stock_filepath(stock):
    return absolute_path([get_stock_dir(stock)])

def get_stock_dir(stock):
    # name = stock + '_' + get_stock_name(stock)
    name = stock
    sep = seperator.windows
    if env.is_linux:
        sep = seperator.linux
    return profile.stock_dir + sep + name

def prepare_stock_dir(stock):
    mkdir(get_stock_filepath(stock))

def absolute_filename(path,name):
    return absolute_path([path, name])

def generate_name(stock,name,suffix):
    # return stock + '_' + name + '_' + suffix
    return stock  + '_' + suffix

def filename(dir,stock,name,suffix):
    return absolute_filename(profile.summary_dir, generate_name(stock, name, suffix))

class Stocker(object):
    def __init__(self,stock,file_suffix,prefix,suffix):
        self.stock = stock
        self.file_suffix = file_suffix
        self.prefix = prefix
        self.suffix = suffix

class StockerHolder(object):
    def __init__(self,stock):
        self.stock = stock
        self.stockers = {}
        self.stockers['primary'] = Stocker(stock, profile.file['primary'], config.prefix['primary'], config.suffix['report'])
        self.stockers['abstract'] = Stocker(stock, profile.file['abstract'], config.prefix['abstract'], config.suffix['html'])
        self.stockers['balance'] = Stocker(stock, profile.file['balance'], config.prefix['balance'], config.suffix['html'])
        self.stockers['income'] = Stocker(stock, profile.file['income'], config.prefix['income'], config.suffix['html'])
        self.stockers['cashflow'] = Stocker(stock, profile.file['cashflow'], config.prefix['cashflow'], config.suffix['html'])
        self.stockers['earning'] = Stocker(stock, profile.file['earning'], config.prefix['primary'], config.suffix['earning'])
        self.stockers['repaying'] = Stocker(stock, profile.file['repaying'], config.prefix['primary'], config.suffix['repaying'])
        self.stockers['growth'] = Stocker(stock, profile.file['growth'], config.prefix['primary'], config.suffix['growth'])
        self.stockers['operation'] = Stocker(stock, profile.file['operation'], config.prefix['primary'], config.suffix['operation'])

def get_stock_name(code):
    return 'media'

def stocker_url(stocker):
    return config.service + stocker.prefix + stocker.stock + stocker.suffix

def stocker_file(stocker):
    stock_name = get_stock_name(stocker.stock)
    file_name = generate_name(stocker.stock,stock_name,stocker.file_suffix + profile.csv)
    return absolute_filename(get_stock_dir(stocker.stock),file_name)

def download_original_files(holder):
    prepare_stock_dir(holder.stock)
    for item in holder.stockers.items():
        stocker = item[1]
        save_file(stocker_url(stocker),stocker_file(stocker))
    print("download original files succeed")

def download_original(stock):
    holder = StockerHolder(stock)
    download_original_files(holder)

def read_dataframe(file):
    pwd = os.getcwd()
    os.chdir(os.path.dirname(file))
    with open(file, 'rb') as f:
        charset = chardet.detect(f.read())
    df = pd.read_csv(os.path.basename(file), header=None, encoding=charset['encoding'])
    os.chdir(pwd)
    return df

def basic_filename():
    return absolute_filename(profile.summary_dir,profile.basic_filename)

def config_filename():
    return absolute_filename(profile.config_dir,profile.config_filename)

def summary_filename(stock):
    stock_name = get_stock_name(stock)
    return filename(profile.summary_dir, stock, stock_name, profile.summary_suffix)

def year_filename(stock):
    stock_name = get_stock_name(stock)
    return filename(profile.summary_dir, stock, stock_name, profile.year_suffix)

def final_filename(stock):
    stock_name = get_stock_name(stock)
    return filename(profile.summary_dir, stock, stock_name, profile.final_suffix)

def merge_original_summary(holder):
    flag = 0
    for item in holder.stockers.items():
        stocker = item[1]
        file = stocker_file(stocker)
        df = read_dataframe(file)
        if flag == 0:
            all = df
        else:
            all = all.append(df[1:], ignore_index=True)
        flag += 1
    summary_file = summary_filename(holder.stock)
    all.to_csv(summary_file)
    print("merge original summary succeed")

def merge_summary(stock):
    holder = StockerHolder(stock)
    merge_original_summary(holder)

def decorate_year_summary(stock):
    summary_file = summary_filename(stock)
    original = read_dataframe(summary_file)
    report_flag_idx = 2 + env.report_have
    year_flag_idx = report_flag_idx + 4 * (env.year_have - 1) + 1
    report_df = original.loc[1:, range(1, report_flag_idx)]
    year_df = original.loc[1:, range(report_flag_idx, year_flag_idx, 4)]
    result = pd.concat([report_df, year_df], ignore_index=True, axis=1, join='inner')
    year_file = year_filename(stock)
    result.to_csv(year_file, index=False, header=False)
    print("decorate year summary succeed")

def parseFloat(x):
    result = 0
    try:
        if not x is np.nan:
            result = float(x)
    except:
        result = 0
    return result

def split(data):
    idxs = np.array(data.split('|'))
    return idxs.astype('int32')

def seriesIx(df,idx):
    series = df.ix[idx]
    series = series[1:df.shape[1]].apply(lambda x: parseFloat(x))
    return series

def withName(cfg,series):
    return np.concatenate(([cfg[fd.name]], series.values), axis=0)

def doPercentage(cfg,df,section,total):
    percentage = section * 100 / total
    percentage = percentage.apply(lambda x: str(round(x, 2)))
    return withName(cfg, percentage)

def percentage(cfg,df,sectionIx,totalIx):
    section = seriesIx(df, sectionIx)
    total = seriesIx(df, totalIx)
    return doPercentage(cfg,df,section,total)

def sumSeries(cfg,df):
    data = split(cfg[fd.data])
    sum = []
    for i in range(0, data.size):
        section = seriesIx(df, data[i])
        if i == 0:
            sum = section
        else:
            sum += section
    return sum

def ix(cfg,df):
    data = int(cfg[fd.index])
    return df.ix[data].values

def assetPercent(cfg,df):
    data = int(cfg[fd.data])
    return percentage(cfg,df,data,indexs.asset)

def sum(cfg,df):
    sum = sumSeries(cfg,df)
    return withName(cfg,sum)

def sub(cfg,df):
    data = split(cfg[fd.data])
    sub = seriesIx(df, data[0])-seriesIx(df, data[1])
    return withName(cfg,sub)

def assetPercentSum(cfg,df):
    sum = sumSeries(cfg,df)
    assets = seriesIx(df, indexs.asset)
    return doPercentage(cfg,df,sum,assets)

def labilityPercent(cfg,df):
    sum = sumSeries(cfg, df)
    labilities = seriesIx(df, indexs.lability)
    return doPercentage(cfg,df,sum,labilities)

def cashRatioSum(cfg,df):
    sum = sumSeries(cfg, df)
    cash = seriesIx(df, indexs.cash)
    percentage = cash / sum
    percentage = percentage.apply(lambda x: str(round(x, 2)))
    return withName(cfg, percentage)

def rotation(cfg,df):
    income = seriesIx(df, indexs.income)
    data = int(cfg[fd.data])
    section = seriesIx(df, data)
    rotation = income/section
    rotation = rotation.apply(lambda x: str(round(x, 2)))
    return withName(cfg, rotation)

def incomePercent(cfg,df):
    data = int(cfg[fd.data])
    return percentage(cfg, df, data, indexs.income)

def incomePercentSum(cfg,df):
    sum = sumSeries(cfg, df)
    income = seriesIx(df, indexs.income)
    return doPercentage(cfg, df, sum, income)

def totalProfit(cfg,df):
    data = int(cfg[fd.data])
    return percentage(cfg, df, data, indexs.profit)

def totalProfitSum(cfg,df):
    sum = sumSeries(cfg, df)
    profit = seriesIx(df, indexs.profit)
    return doPercentage(cfg, df, sum, profit)

def mapping(cfg, df):
    type = cfg[fd.type]
    param = {'cfg':cfg,'df':df}
    return {
            'ix': lambda x: ix(x['cfg'],x['df']),
            'assetPercent': lambda x: assetPercent(x['cfg'],x['df']),
            'sum': lambda x: sum(x['cfg'],x['df']),
            'assetPercentSum': lambda x: assetPercentSum(x['cfg'],x['df']),
            'labilityPercent': lambda x: labilityPercent(x['cfg'],x['df']),
            'rotation': lambda x: rotation(x['cfg'],x['df']),
            'cashRatioSum': lambda x: cashRatioSum(x['cfg'],x['df']),
            'incomePercent': lambda x: incomePercent(x['cfg'],x['df']),
            'incomePercentSum': lambda x: incomePercentSum(x['cfg'],x['df']),
            'totalProfit': lambda x: totalProfit(x['cfg'],x['df']),
            'totalProfitSum': lambda x: totalProfitSum(x['cfg'],x['df']),
            'sub':lambda x: sub(x['cfg'],x['df']),
        }[type](param)

def analysis(stock):
    original = read_dataframe(year_filename(stock))
    config_frame = read_dataframe(config_filename())
    # fields = config_frame[0]
    # print(fields.values)  # 列
    dataframe = original[0:1]
    for i in range(1, config_frame.shape[0]):
        cfg = config_frame.ix[i].values
        series = mapping(cfg, original)
        dataframe.loc[dataframe.shape[0]] = series
    dataframe.to_csv(final_filename(stock), index=False, header=False)
    print("analysis year summary succeed")

def load_stock_year_summary(stock):
    holder = StockerHolder(stock)
    if env.refresh_download:
        download_original_files(holder)
    merge_original_summary(holder)
    decorate_year_summary(stock)
    print("load year summary succeed")

def download_basic():
    df = ts.get_stock_basics()
    df.to_csv(basic_filename())
    print("download basic data succeed")

def run(stock):
    print("runing analysis stock %s ……"%(stock))
    if env.load_before_analysis:
        load_stock_year_summary(stock)
    analysis(stock)

def main():
    if env.analysis_mode:
        stocks = env.stocks
        for stock in stocks:
            run(stock)
    if env.basic_mode:
        download_basic()
if __name__ == '__main__':
    main()
