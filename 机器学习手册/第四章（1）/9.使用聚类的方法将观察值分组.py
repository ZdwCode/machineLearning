import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# 创建模拟的特征矩阵
features, _ = make_blobs(n_samples=50,n_features=2,centers=3,random_state=1)

# 创建数据帧
dataframe = pd.DataFrame(features, columns=['feature_1','feature_2'])

cluster = KMeans(3, random_state=0)

# 使用聚类器
cluster.fit(features)

# 展示聚类的结果
dataframe['group'] = cluster.predict(features)

print(dataframe)

