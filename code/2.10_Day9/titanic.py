import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('2.10_Day9/train.csv')

# # 数据分析
# data.info()
# data.describe().to_csv("2.10_Day9/data_description.csv") # 存入文件

# 数据处理
data['Age'] = data['Age'].fillna(data['Age'].mean()) # 将Age空值填为平均值
data['Embarked'] = data['Embarked'].fillna('S') # 将Embarked空值填为最多的S

# 将字符填为数据，用于以后可能的深度学习
# print(data['Sex'].unique())
# data.loc[data['Sex'] == 'male', 'Sex'] = 1
# data.loc[data['Sex'] == 'female', 'Sex'] = 0

# print(data['Embarked'].unique())
# data.loc[data['Embarked'] == 'S', 'Embarked'] = 0
# data.loc[data['Embarked'] == 'C', 'Embarked'] = 1
# data.loc[data['Embarked'] == 'Q', 'Embarked'] = 2
# print(data.head())

# # 设置中文字体
# plt.rcParams['font.sans-serif'] = ['SimHei'] 
# plt.rcParams['axes.unicode_minus'] = False

# # 总体生还率
# n = data['Survived'].value_counts()
# plt.figure(figsize=(6,6))
# plt.pie(n,autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.4,labeldistance=0.6,
#        shadow=True,explode=[0,0.1],textprops=dict(size=15))
# plt.title('总体生还率')
# plt.show()

# # 性别与生还率
# sex_count = data.groupby(by='Sex')['Survived'].value_counts()
# # print(sex_count)  

# # 男性
# axes1 = plt.subplot(1, 2, 1)
# wedges, texts, autotexts = axes1.pie(sex_count.loc['male'],
#                                      autopct='%.2f%%',
#                                      pctdistance=0.5, 
#                                      shadow=True, 
#                                      explode=[0,0.1], 
#                                      textprops=dict(size=12), 
#                                      colors=['#4682B4', '#87CEEB'], 
#                                      startangle=90)

# # 添加图例
# axes1.legend(wedges, ['死亡', '存活'], title="状态", loc="upper center", 
#              bbox_to_anchor=(0.5, -0.05))
# axes1.set_title('男性生还率')

# # 女性
# axes2 = plt.subplot(1, 2, 2)
# wedges, texts, autotexts = axes2.pie(sex_count.loc['female'][::-1],
#                                      autopct='%.2f%%',
#                                      pctdistance=0.5, 
#                                      shadow=True, 
#                                      explode=[0,0.1], 
#                                      textprops=dict(size=12), 
#                                      colors=['#9400D3', '#FFB6C1'], 
#                                      startangle=90)

# # 添加图例
# axes2.legend(wedges, ['死亡', '存活'], title="状态", loc="upper center", 
#              bbox_to_anchor=(0.5, -0.05))
# axes2.set_title('女性生还率')
# plt.show()

# # 客舱等级与生还率
# pclass_count =  data.groupby(by='Pclass')['Survived'].value_counts()
# # print(pclass_count)  

# # 一等舱
# axes1 = plt.subplot(1, 3, 1)
# wedges, texts, autotexts = axes1.pie(pclass_count.loc[1][::-1],
#                                      autopct='%.2f%%',
#                                      pctdistance=0.5, 
#                                      shadow=True, 
#                                      explode=[0,0.1], 
#                                      textprops=dict(size=10), 
#                                      colors=['#4682B4', '#87CEEB'], 
#                                      startangle=90)

# # 添加图例
# axes1.legend(wedges, ['死亡', '存活'], title="状态", loc="upper center", 
#              bbox_to_anchor=(0.5, -0.05))
# axes1.set_title('一等舱生还率')

# # 二等舱
# axes2 = plt.subplot(1, 3, 2)
# wedges, texts, autotexts = axes2.pie(pclass_count.loc[2],
#                                      autopct='%.2f%%',
#                                      pctdistance=0.5, 
#                                      shadow=True, 
#                                      explode=[0,0.1], 
#                                      textprops=dict(size=10), 
#                                      colors=['#2A9D8F', '#E9C46A'], 
#                                      startangle=90)

# # 添加图例
# axes2.legend(wedges, ['死亡', '存活'], title="状态", loc="upper center", 
#              bbox_to_anchor=(0.5, -0.05))
# axes2.set_title('二等舱生还率')

# # 三等舱
# axes3 = plt.subplot(1, 3, 3)
# wedges, texts, autotexts = axes3.pie(pclass_count.loc[3],
#                                      autopct='%.2f%%',
#                                      pctdistance=0.5, 
#                                      shadow=True, 
#                                      explode=[0,0.1], 
#                                      textprops=dict(size=10), 
#                                      colors=['#9400D3', '#FFB6C1'], 
#                                      startangle=90)

# # 添加图例
# axes3.legend(wedges, ['死亡', '存活'], title="状态", loc="upper center", 
#              bbox_to_anchor=(0.5, -0.05))
# axes3.set_title('三等舱生还率')
# plt.show()

# # 登入港口与生还率
# embarked_count =  data.groupby(by='Embarked')['Survived'].value_counts()
# # print(embarked_count)  

# # Southampton
# axes1 = plt.subplot(1, 3, 1)
# wedges, texts, autotexts = axes1.pie(embarked_count.loc['S'],
#                                      autopct='%.2f%%',
#                                      pctdistance=0.5, 
#                                      shadow=True, 
#                                      explode=[0,0.1], 
#                                      textprops=dict(size=10), 
#                                      colors=['#4682B4', '#87CEEB'], 
#                                      startangle=90)

# # 添加图例
# axes1.legend(wedges, ['死亡', '存活'], title="状态", loc="upper center", 
#              bbox_to_anchor=(0.5, -0.05))
# axes1.set_title('S港登入生还率')

# # Cherbourg
# axes2 = plt.subplot(1, 3, 2)
# wedges, texts, autotexts = axes2.pie(embarked_count.loc['C'][::-1],
#                                      autopct='%.2f%%',
#                                      pctdistance=0.5, 
#                                      shadow=True, 
#                                      explode=[0,0.1], 
#                                      textprops=dict(size=10), 
#                                      colors=['#2A9D8F', '#E9C46A'], 
#                                      startangle=90)

# # 添加图例
# axes2.legend(wedges, ['死亡', '存活'], title="状态", loc="upper center", 
#              bbox_to_anchor=(0.5, -0.05))
# axes2.set_title('C港登入生还率')

# # Queenstown
# axes3 = plt.subplot(1, 3, 3)
# wedges, texts, autotexts = axes3.pie(embarked_count.loc['Q'],
#                                      autopct='%.2f%%',
#                                      pctdistance=0.5, 
#                                      shadow=True, 
#                                      explode=[0,0.1], 
#                                      textprops=dict(size=10), 
#                                      colors=['#9400D3', '#FFB6C1'], 
#                                      startangle=90)

# # 添加图例
# axes3.legend(wedges, ['死亡', '存活'], title="状态", loc="upper center", 
#              bbox_to_anchor=(0.5, -0.05))
# axes3.set_title('Q港登入生还率')
# plt.show()

# # 年龄区间与生还率

# # 划分年龄段
# bins = range(0, 81, 5) # data_description中查看到最大年龄为80岁
# labels = [f"{i}-{i+5}" for i in range(0, 75, 5)] + ["75-80"] # 列表推导式给每个区间起名字
# data['AgeBin'] = pd.cut(data['Age'], bins=bins, labels=labels) # 创建年龄分段的新列

# # 统计生还和死亡人数
# survived_counts = data[data['Survived'] == 1].groupby('AgeBin', observed=False)['Survived'].count()
# dead_counts = data[data['Survived'] == 0].groupby('AgeBin', observed=False)['Survived'].count()
# # 使用 observed=False 确保两个数组元素相同

# # 绘制条形图
# x = np.arange(len(labels)) 
# width = 0.4 # 条形宽度

# plt.figure(figsize=(14, 7))

# plt.bar(x - width/2, dead_counts, width, label='死亡', color='#E63946', edgecolor='black', alpha=0.8)
# plt.bar(x + width/2, survived_counts, width, label='生还', color='#457B9D', edgecolor='black', alpha=0.8)

# plt.title('不同年龄段生还与死亡人数', fontsize=16, pad=20)
# plt.xlabel('年龄区间', fontsize=12)
# plt.ylabel('人数', fontsize=12)

# plt.xticks(x, labels) # 绘制x轴
# plt.grid(axis='y', linestyle='--', alpha=0.5) # 添加水平参考线
# plt.legend()

# plt.tight_layout()
# plt.show()

# # 兄弟姐妹和配偶数量与生还率

# # 划分区间
# bins = range(0, 10) # data_description中查看到最大数量为8个,用9个刻度形成8个区间
# labels = [f"{i}" for i in range(9)] # 列表推导式给每个区间起名字
# data['SibSpBin'] = pd.cut(data['SibSp'], 
#                           bins=range(0, 10), 
#                           labels=[f"{i}" for i in range(9)], 
#                           right=False)
#  # 改为左闭右开确保 0 被包含在新列

# # 统计生还和死亡人数
# survived_counts = data[data['Survived'] == 1].groupby('SibSpBin', observed=False)['Survived'].count()
# dead_counts = data[data['Survived'] == 0].groupby('SibSpBin', observed=False)['Survived'].count()
# # 使用 observed=False 确保两个数组元素相同

# # 绘制条形图
# x = np.arange(len(labels)) 
# width = 0.4 # 条形宽度

# plt.figure(figsize=(14, 7))

# plt.bar(x - width/2, dead_counts, width, label='死亡', color='#E63946', edgecolor='black', alpha=0.8)
# plt.bar(x + width/2, survived_counts, width, label='生还', color='#457B9D', edgecolor='black', alpha=0.8)

# plt.title('不同兄弟姐妹和配偶数量生还与死亡人数对比', fontsize=16, pad=20)
# plt.xlabel('兄弟姐妹和配偶数量', fontsize=12)
# plt.ylabel('人数', fontsize=12)

# plt.xticks(x, labels) # 绘制x轴
# plt.grid(axis='y', linestyle='--', alpha=0.5) # 添加水平参考线
# plt.legend()

# plt.tight_layout()
# plt.show()

# # 票价与生还率
# # 按每 50 元一个区间划分
# fare_bins = range(0, 551, 50) # data_description中查看到最高票价为512
# fare_labels = [f"{i}-{i+50}" for i in range(0, 500, 50)] + ["500+"]
# data['FareBin'] = pd.cut(data['Fare'], bins=fare_bins, labels=fare_labels)

# # 计算每个区间的平均生还率
# fare_survival = data.groupby('FareBin', observed=False)['Survived'].mean()

# # 绘制
# plt.figure(figsize=(12, 6))
# # x轴用区间索引，y轴用生还率
# plt.plot(fare_survival.index, fare_survival.values, marker='o', linestyle='-', color='#2A9D8F', markersize=10)
# plt.scatter(fare_survival.index, fare_survival.values, color='#E76F51', s=100, zorder=5)

# plt.title('不同票价区间的平均生还率', fontsize=15)
# plt.xlabel('票价区间')
# plt.ylabel('生还率')
# plt.xticks()
# plt.grid(True, alpha=0.3)
# plt.show()