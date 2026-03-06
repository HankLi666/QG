import numpy as np

class K_means:
    def __init__(self, k=3, max_iter=300, tol=1e-4):
        self.k = k              # 聚类中心数量
        self.max_iter = max_iter # 最大迭代次数
        self.tol = tol          # 收敛容差

    def fit(self, X):
        # 随机选 k 个点
        samples, features = X.shape
        indices = np.random.choice(samples, self.k, replace=False)
        self.centers = X[indices] # 类变量，方便循环更新簇中心

        for i in range(self.max_iter):
            # 计算距离并归类
            distances = self.distances(X)
            self.labels = np.argmin(distances, axis=1) # 将最小下表记录在 labels里面
            
            # 保存旧中心用于对比收敛情况
            old_centers = self.centers.copy()
            
            # 计算簇中心
            for j in range(self.k):
                group_data = X[self.labels == j] # 将属于该簇的数据提取进来
                if len(group_data) > 0: # 非空检测
                    self.centers[j] = group_data.mean(axis=0)
            
            # 检查是否收敛
            if np.all(np.abs(self.centers - old_centers) < self.tol):
                print(f"在第{i}次迭代时收敛")
                break
        return self
    
    def predict(self, X):
        distances = self.distances(X)
        # 计算测试数据簇标签
        return np.argmin(distances, axis=1)

    def SSE(self, X):
        # 每个样本到每个中心的距离
        distances = self.distances(X) 
        # 每个样本到其最近中心的距离
        min_distances = np.min(distances, axis=1)
        # 返回平方和（SSE）
        return np.sum(min_distances**2)

    # 这个函数看不懂，存个标签在这里，后面学的多了再来重新看
    def score(self, y_true, y_pred):
        """
        y_true: 真实的品种标签 (0, 1, 2)
        y_pred: K-means 聚类出来的标签 (也是 0, 1, 2,但顺序可能不同)
        """
        # 1. 创建一个数组，用来存放“翻译”后的预测标签
        new_pred = np.zeros_like(y_pred)
        
        # 2. 找到 K-means 聚出的所有类别（通常是 [0, 1, 2]）
        cluster_labels = np.unique(y_pred)
        
        for cluster in cluster_labels:
            # 找到被 K-means 分到第 cluster 类的所有样本的下标
            mask = (y_pred == cluster)
            
            # 提取这些样本在原数据中对应的真实品种
            true_labels_in_cluster = y_true[mask]
            
            if len(true_labels_in_cluster) > 0:
                # 关键步骤：用 Numpy 统计这组里哪个品种出现的次数最多（众数）
                # counts 返回每个品种出现的次数，bins 返回品种编号
                counts = np.bincount(true_labels_in_cluster)
                real_species = np.argmax(counts) 
                
                # 把这一组的预测标签全部替换为它对应的真实品种
                new_pred[mask] = real_species
                
        # 3. 计算对齐后的准确率
        return np.mean(new_pred == y_true)

    def distances(self, X):
        # 欧氏距离: sqrt(sum((a-b)^2))
        return np.linalg.norm(X[:, np.newaxis] - self.centers, axis=2)

