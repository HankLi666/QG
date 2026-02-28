import numpy as np

# 矩阵运算
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 矩阵乘法
result = np.dot(A, B) 
print(result)

# 逆矩阵
inv_A = np.linalg.inv(A)
print(inv_A)


# 梯度模拟
# f(x, y) = x^2 + y^2
def f(x, y):
    return x**2 + y**2

# 梯度 (2x, 2y)
def gradient(x, y):
    return np.array([2*x, 2*y])

# 初始点
point = np.array([10.0, 10.0])
learning_rate = 0.1

for i in range(10):
    grad = gradient(point[0], point[1])
    point = point - learning_rate * grad  # 往梯度的反方向走
    print(f"第 {i+1} 步: 位置 {point}, 函数值 {f(point[0], point[1]):.4f}")
print('越来越接近极小值')