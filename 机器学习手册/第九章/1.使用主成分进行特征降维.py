"""使用sklearn的主成分分析工具PCA来保留信息量 减少特征数量"""
from sklearn import datasets
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# 加载数据集
digits = datasets.load_digits()
print(digits.keys())
print(digits['target'])
print(digits['data'][0].shape)
fig, axes = plt.subplots(3, 3)
for i in range(3):
    for j in range(3):
        axes[i][j].set_title(digits['target'][i*j])
        axes[i][j].imshow(digits['data'][i*j].reshape(8,8))
plt.show()

# 标准化特征矩阵
standardScale = StandardScaler()
feature = standardScale.fit_transform(digits.data)

# 使用pca进行降维
pca = PCA(n_components=0.99,whiten=True)
# pca = PCA(n_components=50,whiten=True,svd_solver='randomized')
# 执行pca
feature_pca = pca.fit_transform(feature)
print(feature_pca.shape)