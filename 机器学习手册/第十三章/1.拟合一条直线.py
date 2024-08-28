import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

# 加载数据集
boston = load_boston()
feature = boston.data[:,[3,5,7]]
target = boston.target
# 创建线性回归对象
regression = LinearRegression()
# 拟合
regression.fit(feature,target)
predict = regression.predict(feature)
score = 1/len(target) * np.sum(np.square(predict-target))
print(score)
print(regression.coef_)
