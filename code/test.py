import numpy as np

class MyLinearRegression:
    def __init__(self, method='ols', lr=0.01, epochs=1000):
        self.method = method    # 'ols' (解析解) 或 'gd' (梯度下降)
        self.lr = lr            # 学习率
        self.epochs = epochs    # 迭代次数
        self.w = None           # 权重系数 (包含偏置)

    def fit(self, X, y):
        # 1. 预处理：在 X 第一列加上全为 1 的常数列 (对应截距项 w0)
        X = np.insert(X, 0, 1, axis=1)
        m, n = X.shape
        y = y.reshape(-1, 1)

        if self.method == 'ols':
            # 解析解公式: w = (X^T X)^-1 X^T y
            self.w = np.linalg.inv(X.T @ X) @ X.T @ y
            
        elif self.method == 'gd':
            # 梯度下降法
            self.w = np.zeros((n, 1)) # 初始化参数
            for i in range(self.epochs):
                # 计算预测值和误差
                y_pred = X @ self.w
                error = y_pred - y
                # 计算梯度: (1/m) * X^T * (Xw - y)
                gradient = (1/m) * (X.T @ error)
                # 更新参数
                self.w -= self.lr * gradient
                
    def predict(self, X):
        X = np.insert(X, 0, 1, axis=1)
        return X @ self.w

    def score(self, y_true, y_pred):
        # 计算 R^2 评价指标
        u = ((y_true - y_pred) ** 2).sum()
        v = ((y_true - y_true.mean()) ** 2).sum()
        return 1 - u/v