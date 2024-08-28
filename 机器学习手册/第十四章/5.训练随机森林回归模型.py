from sklearn.ensemble import RandomForestRegressor
from sklearn import datasets
# 加载数据
boston = datasets.load_boston()
feature = boston.data[:,0:2]
target = boston.target
print(type(feature))
print(target)
# 创建随机森林回归对象
randomforest = RandomForestRegressor(random_state=0, n_jobs=1)
# 训练模型
# model = randomforest.fit(feature,target)