"""
    对于分类型特征，计算每个特征和目标向量的卡方统计量
    对于数值型特征，计算每个特征与目标向量的方差分析F值
"""
from sklearn import datasets
from sklearn.feature_selection import SelectKBest,chi2,f_classif
iris = datasets.load_iris()

features = iris.data
target = iris.target

# 将分类数据转化为整型
features = features.astype(int)

# 创建卡方统计量
chi2_selector = SelectKBest(chi2,k=2)
features_best = chi2_selector.fit_transform(features,target)

# 显示结果
print(features_best.shape)

# 对于数值型数据 计算F值
features = iris.data
fvalue_selector = SelectKBest(f_classif,k=2)
features_best = fvalue_selector.fit_transform(features,target)
# 显示结果
print(features_best.shape)