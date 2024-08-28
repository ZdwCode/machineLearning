import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.feature_selection import SelectFromModel
# 加载数据
iris = datasets.load_iris()
features = iris.data
target = iris.target

# 创建随机森林分类器
randomforest = RandomForestClassifier(random_state=0,n_jobs=1)
# 创建随机森林分类器
selector = SelectFromModel(randomforest,threshold=0.3)
# 使用选择器创建新的特征矩阵
features_important = selector.fit_transform(features,target)
model = randomforest.fit(features_important,target)