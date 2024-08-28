import numpy as np
from sklearn import preprocessing

x = np.array([[2, 3],
              [2, 3],
              [2, 3],
              ])

def add_ten(x):
    return x+10
# 对特征的每个值进行一次操作 类似于pandas的apply方法
ten_transformer = preprocessing.FunctionTransformer(add_ten)

x_ten_transformer = ten_transformer.transform(x)

print(x_ten_transformer)