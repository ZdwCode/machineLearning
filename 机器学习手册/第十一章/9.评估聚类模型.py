"""使用轮廓系数来评估聚类模型"""
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

featuers,_ = make_blobs(n_samples=1000,n_features=10,centers=2,cluster_std=0.5,shuffle=True,random_state=1)
model = KMeans(n_clusters=2,random_state=1).fit(featuers)

target_predicted = model.labels_

# 评估模型
scores = silhouette_score(featuers,target_predicted)
print(scores)