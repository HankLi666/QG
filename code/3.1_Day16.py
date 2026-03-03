import numpy as np

# 直接计算

# 激活函数
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 输入 x, w, b
x = [1.0, 2.0, 3.0]
w = [0.1, 0.2, 0.3]
b = 0.5

# 计算
z = x[0]*w[0] + x[1]*w[1] + x[2]*w[2] + b
a = sigmoid(z)
print(a)

# 矩阵计算

# 输入 x, w, b
x = np.array([1.0, 2.0, 3.0])
w = np.array([0.1, 0.2, 0.3])
b = 0.5

# 计算
z = np.dot(w, x) + b
a = sigmoid(z)
print(a) 

# 向前传播模拟

# 输入层数据
x = [1.0, 2.0, 3.0]

# 隐藏层参数 (2个神经元)
w1 = np.array([[0.1, 0.2, 0.3], 
               [0.4, 0.5, 0.6]])
b1 = np.array([0.1, 0.2])

# 输出层参数
# w2 的维度是 (1, 2), 对应隐藏层的2个输入
w2 = np.array([0.7, 0.8])
b2 = np.array([0.9])

# 计算
z1 = np.dot(w1, x) + b1
a1 = sigmoid(z1)

z2 = np.dot(w2, a1) + b2
a2 = sigmoid(z2)
print(a2)