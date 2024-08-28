import numpy as np
from sklearn import preprocessing

x = np.array([[2, 3],
              [2, 3],
              [2, 3],
              ])
# 当特征和目标值（预测值）之间存在非线性关系时，就需要创建多项式特征
polynomial_interaction = preprocessing.PolynomialFeatures(degree=3, include_bias=False,interaction_only=True)

x_polynomial_interaction = polynomial_interaction.fit_transform(x)

print(x_polynomial_interaction)