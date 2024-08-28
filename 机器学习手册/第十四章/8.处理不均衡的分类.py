import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets

# 加载数据
iris = datasets.load_iris()
features = iris.data
target = iris.target

# 删除前40个样本获得高度不均衡的数据
features = features[40:,:]
target = target[40:]

#
tartget = np.where((target==0),0,1)

# 创建随机森林分类器对象
randomforest = RandomForestClassifier(random_state=0,n_jobs=1,class_weight="balanced")

# 训练模型
randomforest.fit(features,target)