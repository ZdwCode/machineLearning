from sklearn import datasets
import numpy as np
# 2.1 加载样本数据集
digits = datasets.load_digits()
features = digits.data
target = digits.target

print(features[:10])
print(target[:10])
# 2.2 创建仿真数据集
from sklearn.datasets import make_regression
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 使用make_regression来创造数据
features, target, coeffcients = make_regression(n_samples=5000,
                                                n_features=3,
                                                n_informative=3,
                                                n_targets=1,
                                                noise=0.0,
                                                coef=True,
                                                random_state=1)
print(features[:10, 0:1])
x = features[:, 0:1]
y = features[:, 1:2]
z = features[:, 2:3]
print(target[:10])
#print(coeffcients)
print(np.dot(features[:10],coeffcients))
# ax.scatter(xs=x,ys=y,zs=z)
# plt.show()

# 使用make_classsification创建仿真数据集来做分类
from sklearn.datasets import make_classification
features,target = make_classification(n_samples=5000,
                                      n_features=3,
                                      n_informative=3,
                                      n_redundant=0,
                                      n_classes=2,
                                      weights=[0.1,0.9],
                                      random_state=1
                                      )
x = features[:, 0:1]
y = features[:, 1:2]
z = features[:, 2:3]
ax.scatter(xs=x,ys=y,zs=z)
plt.show()

# 使用make_blob来创造仿真的聚类数据
from sklearn.datasets import make_blobs
features,target = make_blobs(n_samples=1000,
                             n_features=2,
                             centers=3,
                             cluster_std=0.5,
                             shuffle=True,
                             random_state=1)
# print('---')
# print(features)
plt.scatter(features[:,0:1],features[:,1:2],c=target)
plt.show()

# 2.3 加载cvs文件
import pandas as pd
# pd.read_csv()
# 2.4 记载excel文件
# pd.read_excel()
# 2.5 加载json文件
# pd.read_json()
# 2.6 查询sql文件
