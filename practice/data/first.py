'''
Pandas base Opts
23种Pandas核心操作
'''
import pandas as pd
import numpy as np
from tabulate import tabulate

# 1、基本数据集操作
# （1）读取 CSV 格式的数据集
df = pd.read_csv('csv/train.csv')
print(df)
# （2）读取 Excel 数据集
# pd.read_excel("excel_file")
# （3）将 DataFrame 直接写入 CSV 文件
df.to_csv("csv/data.csv", sep=",", index=False)
# （4）基本的数据集特征信息
info = df.info()
print(info)
# （5）基本的数据集统计信息
description = df.describe()
print(description)
# (6) 将 DataFrame 输出到一张表
print(tabulate(df.head(10), headers = df.columns, tablefmt='grid'))
# 当「print_table」是一个列表，其中列表元素还是新的列表，「headers」为表头字符串组成的列表。
# （7）列出所有列的名字 pandas.core.indexes.base.Index → ndarray
cols = df.columns
print(cols)
# 2、基本数据处理
# （8）删除缺失数据
# how = any 删除了包含任何 NaN 值的给定轴，选择 how=「all」会删除所有元素都是 NaN 的给定轴
# axis = 0 行 axis = 1 列
df = df.dropna(axis=0, how='any')
# （9）替换缺失数据
# 使用 value 值代替 DataFrame 中的 to_replace 值，其中 value 和 to_replace 都需要我们赋予不同的值
# df['gender'].replace([0,1,2],[None,'male','famale'],inplace=True)
df['gender_str'] = df['gender'].replace([0,1,2],[np.nan,1,2])
# （10）检查空值 NaN
# 检查缺失值，即数值数组中的 NaN 和目标数组中的 None/NaN。
df['gender_nan'] = pd.isnull(df['gender_str'])
print('Gender is nan record num:',len(df.loc[df['gender_nan']==True]))
# （11）删除特征
df = df.drop('gender_str', axis=1)
df = df.drop('gender_nan', axis=1)
# （12）将目标类型转换为浮点型
# 将目标类型转化为数值从而进一步执行计算，在这个案例中为字符串。
pd.to_numeric(df["gender"], errors='coerce')
# （13）将 DataFrame 转换为 NumPy 数组
print(df.values)
# （14）取 DataFrame 的前面「n」行
print(df.head(5))
# （15）通过特征名取数据
age = df.loc[:,'age']
print(age)
# 3、DataFrame 操作
# （16）对 DataFrame 使用函数
# 该函数将令 DataFrame 中「height」行的所有值乘上 2：
df["age_double"] = df['age'].apply(lambda age: 2 * age)
# （17）重命名行
df.rename(columns = {df.columns[0]:'service_type'}, inplace=True)
print(tabulate(df.head(5), headers = df.columns, tablefmt='grid'))
# （18）取某一列的唯一取值
print(df["service_type"].unique())
print(df["service_type"].nunique())
# （19）访问子 DataFrame
new_df = df[["service_type", "current_service"]]
new_df["current_service"] = new_df["current_service"].apply(int).apply(str)
print(new_df.info())
print(tabulate(new_df.head(5), headers =["no","service_type", "current_service"], tablefmt='grid'))
type_service_map = new_df.drop_duplicates(["service_type", "current_service"]).reset_index(drop=True)
print(type_service_map)
# （20）总结数据信息
# # Sum of values in a data frame
# df.sum()
# # Lowest value of a data frame
# df.min()
# # Highest value
# df.max()
# # Index of the lowest value
# df.idxmin()
# # Index of the highest value
# df.idxmax()
# # Statistical summary of the data frame, with quartiles, median, etc.
# df.describe()
# # Average values
# df.mean()
# # Median values
# df.median()
# # Correlation between columns
# df.corr()
# # To get these values for only one column, just select it like this#
# df["age"].median()
# （21）给数据排序
type_service_map.sort_values(by=['service_type', "current_service"],ascending = True,inplace = True)
print(type_service_map.reset_index(drop=True))
# （22）布尔型索引
print(type_service_map[type_service_map["service_type"] == 4])
# （23）选定特定的值
print(type_service_map.loc[0, 'current_service'])
