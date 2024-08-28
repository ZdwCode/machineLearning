'''使用scikit-learn中的DecisionTreeClassifier'''
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets

# 加载数据
iris = datasets.load_iris()
features = iris.data
target = iris.target

# 创建决策树分类器对象
decisiontree = DecisionTreeClassifier(random_state=0)

# 训练模型
model = decisiontree.fit(features,target)

