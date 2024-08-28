import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.datasets import make_blobs

# 创建模拟数据
features,_ = make_blobs(n_samples=10,n_features=2,centers=1,random_state=1)

# 常用的方法是假设数据是正态分布的，基于这个假设，
# 在数据周围“画”一个椭圆，将所有处于椭圆内的观察值视为正常值
# （标注为1），将所有处于椭圆外的观察值视为异常值（标注为-1）：

# 创建几个极端的值
features[0,0]=10000
features[0,1]=10000

# 创建异常值识别器
outlier_detector = EllipticEnvelope(contamination=.2) # contamination（污染指数）参数，表示异常值在观察值中的比例

# 拟合识别器
outlier_detector.fit(features)

# 预测出异常值
print(features)
outliner_number = outlier_detector.predict(features)

print(outliner_number)