## numpy库的导入
[ numpy官方文档l](https://numpy.org/doc/stable/user/index.html#use)

```python
import numpy as np
```

---
## 1. 核心概念：ndarray

NumPy 的核心是 **ndarray**（可理解为数组），支持**向量化操作**，且内存布局连续，速度极快。
每个 `ndarray` 对象自带“名片”：

- **`dtype` (Data Type)**: 数组中元素的类型。

- **`ndim` (Number of Dimensions)**: 数组的秩（维度的数量）。

	> 向量的 `ndim` 为 1，矩阵的 `ndim` 为 2。
### 常用初始化方法

```python
# 从列表创建
arr = np.array([1, 2, 3, 4]) 

# 创建随机数矩阵
rand_arr = np.random.rand(2, 3)
```
#### 用arange创建等差数列
与range函数类似
```python
arr = np.range(12)  # 生成一个从0开始，到 12-1 结束，步长为1的一维数组
arr = np.arange(0, 10, 2)  # 类似 for(int i=0; i<10; i+=2)
```
#### 用 linspace 创建等分数列
**指定点数**，常用于绘图 X 轴
```python
np.linspace(start, stop, num)
x = np.linspace(0, 2 * np.pi, 100) # 在 0 到 2π 之间生成 100 个等间距的点
```

### 特殊矩阵构建

除了 `np.array()`，还有这些快捷函数：

|**函数**|**功能**|**类似 C 逻辑**|
|---|---|---|
|`np.zeros((3,4))`|全 0 矩阵|`calloc(12, sizeof(int))`|
|`np.ones((2,2))`|全 1 矩阵|循环赋值 1|
|`np.eye(3)`|**单位矩阵** (Identity)|对角线 `i==j` 为 1，其余 0|
|`np.full((2,2), 7)`|全指定值矩阵|循环赋值 7|

---

## 2. 数组的形状与转换

- **`shape`**: 查看维度（返回一个元组）。

- **`reshape()`**: 改变维度（数据总量不变）。

- **`T`**: 矩阵转置。

```PYTHON
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)  # 输出 (2, 3)

# 转换成 3行2列
b = a.reshape(3, 2)

# 转置
c = a.T  # 变成 (3, 2)
```
### reshape中 -1 的用法

[![pZ7maFK.png](https://s41.ax1x.com/2026/02/09/pZ7maFK.png)](https://imgchr.com/i/pZ7maFK)
- **含义**：占位符，表示“让 NumPy 自动计算此维度的长度”。
- **约束**：一个 reshape 调用中 **只能出现一个 -1**（否则 NumPy 无法解出唯一的解）。
- **常见场景**：
    * `arr.reshape(-1)`：彻底展平为一维。
    * `arr.reshape(-1, 1)`：将一维向量转为“列矩阵”。
    * `arr.reshape(1, -1)`：将一维向量转为“行矩阵”。
```python
arr = np.arange(12) # 长度为 12 
a = arr.reshape(3, -1) # 自动计算列数：12/3 = 4 -> (3, 4) 
b = arr.reshape(-1, 2) # 自动计算行数：12/2 = 6 -> (6, 2)
```

## 3. 切片与索引 

- **格式**: `array[行起始:行结束, 列起始:列结束]`

```python
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 获取第一行
row1 = data[0, :]

# 获取第二列
col2 = data[:, 1]

# 获取左上角 2x2 子矩阵
sub_matrix = data[0:2, 0:2]
```

---

## 4. 矩阵运算 

避开了 Python 原生的慢速循环，调用了底层的 C 和 Fortran 库，使得运算效率极快

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
```
### 矩阵乘法
```python
result = np.dot(A, B) 
# 或者
result = A @ B 
```
### 矩阵转置
```python
result = A.T
# ([[3, 4], [1, 2]])
```
### 矩阵的逆
- `np.linalg.inv`
- **只有方阵且行列式不为 0 才有逆**
```python
inv_A = np.linalg.inv(A)
```
### 矩阵存取
除了基础切片，NumPy 支持 **布尔索引**

```python
data = np.array([1, 5, 8, 10, 2])
# 找出所有大于 5 的数
print(data[data > 5])  # 输出 [8, 10]
```
---

## 5. 广播机制

这是 NumPy 的“自动伸缩”功能。当两个数组形状不同时，NumPy 尝试在较小的维度上“复制”数据以匹配大数组。

- **规则**: 如果两个数组的后缘维度（从右往左看）的轴长度相符，或其中一方长度为 1，则可以广播。

> **例子**：一个矩阵加一个标量，标量会被广播到矩阵的每一个元素上。

```python
m = np.array([1, 2, 3])
print(m + 10) # 输出 [11, 12, 13]
```