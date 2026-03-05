import numpy as np
import pandas as pd
from linear_regression import linear_regression

# # 将数据存到本地
# url = "http://lib.stat.cmu.edu/datasets/boston"
# df = pd.read_csv(url, sep="\s+", skiprows=22, header=None)
# df.to_csv('Boston.csv', index=False)

data = pd.read_csv('3.3_Day18/Boston.csv')

# 合并数据
X = np.hstack([data.values[::2, :], data.values[1::2, :2]])
y = data.values[1::2, 2]

# 拼接columns
complete_data = np.column_stack([X, y])
columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# 创建DataFrame，方便数据分析和特征处理
data = pd.DataFrame(complete_data, columns=columns)
# data.describe().to_csv("3.3_Day18/data_description.csv") # 存入文件

# 提取数据
X = data.drop('MEDV', axis=1).values
y = data['MEDV'].values

# 设置随机种子保证结果可复现
np.random.seed(42)
indices = np.arange(X.shape[0])
np.random.shuffle(indices) # 打乱数据

# 计算切分点
split_idx = int(X.shape[0] * 0.8)
train_idx, test_idx = indices[:split_idx], indices[split_idx:]

X_train, X_test = X[train_idx], X[test_idx]
y_train, y_test = y[train_idx], y[test_idx]

# 数据归一化
# 均值和标准差
mean = np.mean(X_train, axis=0)
std = np.std(X_train, axis=0)

# 测试集使用训练集的 mean 和 std，以模拟真实预测场景
X_train_scaled = (X_train - mean) / std
X_test_scaled = (X_test - mean) / std

# 使用解析解
model = linear_regression(method='ols')
# 使用梯度下降，学习率0.1，迭代 2000 次
model = linear_regression(method='ols', lr = 0.1, epochs=2000)

# 传入数据
model.fit(X_train_scaled, y_train)

# 预测
y_pred = model.predict(X_test_scaled)

# 评价
r2 = model.score(y_test.reshape(-1, 1), y_pred)

print(f"权重系数 (w):\n{model.w}")
print(f"测试集 R^2 分数: {r2:.4f}")

# 评价：
# 两种线性回归模型 R^2 分数均为0.6873，查阅AI得知处于标准线性回归的基准线上，
# 后续想提升可以考虑加入正则化与神经网络