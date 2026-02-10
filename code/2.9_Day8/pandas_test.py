import pandas as pd

# 解析 url 读取数据
url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

df = pd.read_csv(url)

# 查看前 5 行，确认是否读取成功
print(df.head())

# 存入本地
df.to_csv('2.9_Day8/housing.csv', index=False)

# 检查空值，将空数据存进 missing_values.csv 
missing_data = df.isnull().sum()
missing_data.to_csv("2.9_Day8/missing_values.csv")

# 将 total_bedrooms 中的空值填为该列的中位数
median_value = df["total_bedrooms"].median() # 计算中位数

# 填补 total_bedrooms 这一列，并原地修改
df["total_bedrooms"].fillna(median_value, inplace=True) 

# 数据分析
df.info()
df.describe().to_csv("2.9_Day8/data_description.csv") # 存入文件