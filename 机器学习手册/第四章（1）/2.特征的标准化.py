import numpy as np
from sklearn import preprocessing
x = np.array([[-1000.1],
              [-200.2],
              [500.5],
              [600.6],
              [9000.9],])

scaler = preprocessing.StandardScaler()

# 使用
x_standard = scaler.fit_transform(x)

print(x_standard)