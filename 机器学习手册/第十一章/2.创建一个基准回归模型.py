"""
通过哑变量回归模型，可以得到一个预测值，这个值其实就是所有房价的平均值。
这个模型虽然简单，但在实际应用中有其价值。它提供了一个基准，
用于评估其他更复杂的模型是否真正有效。
如果一个复杂模型的表现不如这个简单模型，那么可能需要重新考虑复杂模型的适用性。
"""
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression

boston = datasets.load_boston()
features, targets = boston.data, boston.target

# 划分训练集和测试集
features_train,features_test,targets_train,targets_test = train_test_split(features,targets,random_state=1)

# 创建一个dummgRegressor对象
dummy = DummyRegressor(strategy='mean')

# 训练回归模型
dummy.fit(features_train,targets_train)

# 计算R方得分
score = dummy.score(features_test,targets_test)

print(score)

# 训练自己的模型与基准模型对比 越接近1，就代表特征对目标向量的解释越好（即相关性越高）。
model = LinearRegression()
model.fit(features_train,targets_train)
print(model.score(features_test,targets_test))