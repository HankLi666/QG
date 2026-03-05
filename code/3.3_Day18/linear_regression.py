import numpy as np

class linear_regression:
    # 初始化超参数
    def __init__(self, method='ols', lr=0.01, epochs=1000):
        self.method = method  # 默认为解析解
        self.lr = lr          # 学习率默认为 0.01
        self.epochs = epochs  # 迭代次数默认为 1000 次

    # 训练
    def fit(self, X, y):
        # 在 X 第一列加上全为 1 的常数列
        X = np.insert(X, 0, 1, axis=1)
        m, n = X.shape # m个样本，n个特征
        y = y.reshape(-1, 1) # 转为列矩阵

        if self.method == 'ols':
            self.w = np.linalg.inv(X.T @ X) @ X.T @ y
        elif self.method == 'gd':
            self.w = np.zeros((n, 1)) # 初始化参数为0
            for i in range(self.epochs):
                # 计算梯度: (1/m) * X^T * (Xw - y)
                gradient = (1/m) * (X.T @ (X @ self.w - y))
                # 更新参数
                self.w -= self.lr * gradient

    # 预测
    def predict(self, X):
        X = np.insert(X, 0, 1, axis=1)
        return X @ self.w

    # 评分
    def score(self, y_true, y_pred):
        # 计算 R^2 评价指标
        u = ((y_true - y_pred) ** 2).sum()
        v = ((y_true - y_true.mean()) ** 2).sum()
        return 1 - u/v
