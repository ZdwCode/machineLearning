"""
使用线性判别分析（Linear Discriminant Analysis,LDA）
方法，将特征数据映射到一个可以使类间可分性最大的成分坐标轴上
"""
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
iris = datasets.load_iris()
features = iris.data
target = iris.target

# 创建并运行lda
lda = LinearDiscriminantAnalysis(n_components=1) # n_components cannot be larger than min(n_features, n_classes - 1)
feature_lda = lda.fit(features,target).transform(features)
print(feature_lda.shape)
print(features.shape)
print(target)
# explained_variance_ratio_来查看每个成分保留的信息量
print(lda.explained_variance_ratio_)