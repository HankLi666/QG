## 流程
1. **初始化**：随机选择 $K$ 个点作为初始聚类中心

2. **分配**：计算每个样本到这 $K$ 个中心的距离，离谁近就归为哪一类。

3. **更新**：重新计算每个簇内所有样本的平均值，将其作为新的中心。

4. **递归**：重复步骤 2 和 3，直到收敛
---
## 实战
### 数据导入
利用 `sklearn` 内置的鸢尾花数据集作为实验对象

- **数据集构成**：150 个样本，4 个特征（萼片长/宽、花瓣长/宽），3 个类别

```python
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target  # X 是特征矩阵 (150, 4)，y 是标准答案 (150,)
```
### 计算距离算法优化
为了避免写嵌套循环，利用 Numpy 的广播机制维度扩展
```python
def distances(self, X):
	# 欧氏距离: sqrt(sum((a-b)^2))
	return np.linalg.norm(X[:, np.newaxis] - self.centers, axis=2)
```
- **逻辑拆解**：
    1. **升维**：将样本 $X$ 从 $(150, 4)$ 变为 $(150, 1, 4)$。
    2. **对齐**：中心点 `centers` 形状为 $(3, 4)$。
    3. **计算**：`diff = X[:, np.newaxis, :] - self.centers`。
- Numpy 自动将 $X$ 复制 3 份，将 `centers` 复制 150 份。一行代码直接算出 **450 组对应的坐标差值**
### SSE评价机制
由于是无监督学习，通过内部评价来判断聚类的**紧凑度**
$SSE$ = 最近中心距离平方和
