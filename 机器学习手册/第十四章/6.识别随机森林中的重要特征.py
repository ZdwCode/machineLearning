import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
# 加载数据
iris = datasets.load_iris()
features = iris.data
target = iris.target

# 创建随机森林分类器
randomforest = RandomForestClassifier(random_state=0,n_jobs=1)
# 训练模型
randomforest.fit(features,target)

# 计算特征重要性
importance = randomforest.feature_importances_

# 排序
print(np.argsort(importance)) # 返回的是索引
indices= np.argsort(importance)[::-1]
# 按照特征的重要性对特征名称重新排序
print(iris.feature_names)
names = [iris.feature_names[i] for i in indices]
print(names)
# 画图
plt.figure()
#
plt.title('Feature Importance')
#
plt.bar(range(features.shape[1]),importance[indices])

plt.xticks(range(features.shape[1]),names)

plt.show()