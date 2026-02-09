import numpy as np


# 创建一个形状为 (3,4) 的二维数组，元素为 0-11 的连续整数

arr1 = np.arange(12).reshape(3, 4)

# 查看数组的 shape 、 dtype 、 ndim 属性

print(arr1.shape)
print(arr1.dtype)
print(arr1.ndim)

# 将数组变形为 (4,3)，并展平为一维数组

arr1 = arr1.T
print(arr1)
arr1 = arr1.reshape(-1)
print(arr1)
