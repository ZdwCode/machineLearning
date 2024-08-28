from sklearn.tree import DecisionTreeRegressor
from sklearn import datasets
# 加载数据
boston = datasets.load_boston()
feature = boston.data[:,0:2]
target = boston.target


# 创建决策树分类对象
decisiontree = DecisionTreeRegressor(random_state=0)
# 训练模型
model = decisiontree.fit(feature,target)

