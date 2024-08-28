from sklearn.datasets import load_boston
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
boston = load_boston()
feature = boston.data[:,0:2]
target = boston.target

# 创建交互特征
interaction = PolynomialFeatures(degree=3,interaction_only=True,include_bias=False)
# 数据增强
feature_interaction = interaction.fit_transform(feature)
print(feature_interaction)

regression = LinearRegression()
regression.fit(feature_interaction,target)
predict = regression.predict(feature_interaction)
score = 1/len(target) * np.sum(np.square(predict-target))
print(score)