"""使用KNN算法来填充缺失值"""
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X = np.array([[0, 2.10, 1.45],
              [1, 1.18, 1.33],
              [0, 1.22, 1.27],
              [1, -0.21, -1.19],
              ])

x_with_nan = np.array([[np.nan, 0.87, 1.31],
                       [np.nan, -0.67, -0.22]])


# 训练KNN分类器
clf = KNeighborsClassifier(3, weights="distance")
trained_model = clf.fit(X[:,1:],X[:,0])

# 预测缺失值的分类
impute_values = trained_model.predict(x_with_nan[:,1:])
print(impute_values)
print(type(impute_values))
# 将所预测的分类和他们的其他特连接起来
X_with_impute = np.hstack((impute_values.reshape(-1,1),x_with_nan[:,1:]))
print(impute_values.reshape(-1,1))

# 连接两个矩阵
result = np.vstack((X_with_impute,X))
print(result)