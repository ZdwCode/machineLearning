import numpy as np
import pandas as pd
from sklearn import preprocessing

# 4.1 特征的缩放
feature = np.array([[-500,2],
                    [-100,3],
                    [0,4],
                    [100,5],
                    [900,6]])
# 相当于创建一个缩放器
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))
# 使用这个缩放器
scaled_feature = minmax_scale.fit_transform(feature)
print(scaled_feature)  # x = (x-min)/max-min
# 4.2 特征的标准化
# 创建一个表转化器
scaler = preprocessing.StandardScaler()
# 使用这个转化器
standardized = scaler.fit_transform(feature)
print(standardized)

# 4.3 归一化观察值
feature2 = np.array([[0.5,0.5],
                     [1.1,3.4],
                     [10.9,3.3]])

# 创建一个归一化器
scaler = preprocessing.Normalizer()
print(scaler.transform(feature2))
scaler = preprocessing.Normalizer(norm='l1')
print(scaler.transform(feature2))

# 4.4 生成多项式和交互特征
feature = np.array([[2,3],
                    [2,3],
                    [2,3]])
polynomial_interaction = preprocessing.PolynomialFeatures(degree=2,include_bias=False)
print(polynomial_interaction.fit_transform(feature))

polynomial_interaction = preprocessing.PolynomialFeatures(degree=2,include_bias=True,interaction_only=True)
print(polynomial_interaction.fit_transform(feature))

# 4.5 转换特征
from sklearn.preprocessing import FunctionTransformer

# 创建一个特征矩阵
features = np.array([[2,3],
                     [2,3],
                     [2,3]])

def add_ten(x):
    return x+10

ten_transformer = FunctionTransformer(add_ten)

result = ten_transformer.transform(features)
print(result)

# 4.6 识别异常值
from sklearn.covariance import EllipticEnvelope
from sklearn.datasets import make_blobs

# 创建聚类仿真数据
features,_= make_blobs(n_samples=10,
                       n_features=2,
                       centers=1,
                       random_state=1)

# 将第一个观察值的特征给替换为极端值
features[0,0]=1000
features[0,1]=1000

# 创建一个识别器
outlier_detector = EllipticEnvelope(contamination=.1) # 识别器需要一个污染指数

# 拟合识别器
outlier_detector.fit(features) # 创建了识别器之后 需要先拟合

# 预测异常值
result = outlier_detector.predict(features)
print(result)

# 4.7 处理异常值
# 第一种方法就是丢弃异常值 使用pandas筛选的功能删除某些行
houses = pd.DataFrame()
houses['Price'] = [1000,2000,3000,5000]
houses['Bathrooms'] = [2,3.5,2,116]
houses['Sqare_feet'] = [20,30,40,50]

# 删除厕所大于20的值
print(houses[houses['Bathrooms']<20])
# 第二种方式是标记为异常值
houses['Outlier'] = np.where(houses['Bathrooms']<20,0,1)
print(houses)

# 4.8 将特征离散化
# 第一种最简单的离散化就是特征二值法
from sklearn.preprocessing import Binarizer
age = np.array([[6],
                [12],
                [15],
                [20],
                [30]])

# 创建二值化器
binarizer = Binarizer(threshold=18)
print(binarizer.fit_transform(age))