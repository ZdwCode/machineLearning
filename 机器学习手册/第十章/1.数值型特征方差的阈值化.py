"""从一组数值型特征中移除方差较小的特征"""
from sklearn import datasets
from sklearn.feature_selection import VarianceThreshold
iris = datasets.load_iris()

features = iris.data
target = iris.target
print(features)
# 创建VarianceThreshold对象 方差过滤器
thresholder = VarianceThreshold(threshold=0.6)

# 创建大方差特征矩阵
features_high_variance = thresholder.fit_transform(features) # 改方法会删除方差低于某个阈值的特征
print(features_high_variance)


"""第一，方差不是中心化的（它的单位是特征单位的平方）。因此，如果特征数据集中特征的单位不同
（例如，一个特征以年为单位，而另一个特征以美元为单位），那么VT法就无法起作用。第二，
方差的阈值是手动选择的，所以必须依靠人工来选择一个合适的阈值。"""