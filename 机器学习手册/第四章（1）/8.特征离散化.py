import numpy as np
from sklearn import preprocessing

age = np.array([[6],
                [12],
                [20],
                [36],
                [65],])

# 创建一个二值化器 直接根据单个阈值二值化
binarizer = preprocessing.Binarizer(threshold=18)

# 转化特征
age_binarizer = binarizer.fit_transform(age)
print(age_binarizer)

# 根据多个阈值将特征离散化
age_digitize = np.digitize(age,[20,30,64])
print(age_digitize)