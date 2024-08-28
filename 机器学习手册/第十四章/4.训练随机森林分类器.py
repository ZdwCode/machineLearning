from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets

# 加载数据
iris = datasets.load_iris()
features = iris.data
target = iris.target

# 创建随机森林分类器
randomforest = RandomForestClassifier(random_state=0,n_jobs=1)

# 训练模型
model = randomforest.fit(features,target)