from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()

features, targets = iris.data, iris.target

# 划分训练集和测试集
features_train,features_test,targets_train,targets_test = train_test_split(features,targets,random_state=1)
# 创建dummyClassifier
dummy = DummyClassifier(strategy='uniform',random_state=1)
# 训练
dummy.fit(features_train,targets_train)

# 得分
score = dummy.score(features_test,targets_test)
print(score)

#
classifier = RandomForestClassifier()
classifier.fit(features_train,targets_train)
score = classifier.score(features_test,targets_test)
print(score)