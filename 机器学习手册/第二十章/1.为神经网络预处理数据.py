from sklearn import preprocessing
import numpy as np

# 创建特征
features = np.array([[-100.1,3240.1],
                     [-200.2,-234.1],
                     [5000,150.1],
                     [6000,-125.1],
                     [9000,-673.1],])

scaler = preprocessing.StandardScaler()

features_standardized = scaler.fit_transform(features)

print(features_standardized)