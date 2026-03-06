import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from K_means import K_means

iris = load_iris()
X, y = iris.data, iris.target

# # 检查数据是否导入
# df = pd.DataFrame(X, columns=iris.feature_names)
# df.info()
# print(df.head()) # 查看前5行

# 设置随机种子保证结果可复现
np.random.seed(42)

# 生成打乱的索引
indices = np.random.permutation(X.shape[0])

# 计算切分点
split_idx = int(X.shape[0] * 0.8)
train_idx, test_idx = indices[:split_idx], indices[split_idx:]
X_train, X_test = X[train_idx], X[test_idx]
y_train, y_test = y[train_idx], y[test_idx]

# 数据归一化
mean = np.mean(X_train, axis=0)
std = np.std(X_train, axis=0)

# 测试集使用训练集的 mean 和 std，以模拟真实预测场景
X_train_scaled = (X_train - mean) / std
X_test_scaled = (X_test - mean) / std

model = K_means(k=3)
model.fit(X_train_scaled)

train_result = model.SSE(X_train_scaled)
print(f"训练集 SSE: {train_result}")

y_pred = model.predict(X_test_scaled)
rate = model.score(y_test, y_pred)
print(f"准确率是{rate:.3f}")