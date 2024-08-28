import numpy as np
from sklearn import preprocessing


feature = np.array([[0.5,0.5],
              [1.1,3.4],
              [1.5,20.2],
              [1.63,34.4],
              [10.9,3.3]
              ])
# feature = np.array([[-500.5],
#                     [-100.1],
#                     [0],
#                     [100.1],
#                     [500.5],])

# 创建一个缩放器
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0,1))

# 使用所放弃缩放特征的值
scaled_feature = minmax_scale.fit_transform(feature)

print(scaled_feature)