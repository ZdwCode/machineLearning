"""使用kernelPCA对线性不可分的数据集进行降维"""
from sklearn import datasets
from matplotlib import pyplot as plt
from sklearn.decomposition import KernelPCA
features,targets = datasets.make_circles(n_samples=1000,random_state=1,noise=0.1,factor=0.1)

print(features)
print(targets)
features_targets_1_x = []
features_targets_1_y = []
features_targets_0_x = []
features_targets_0_y = []
for index in range(len(features)):
    if targets[index] == 0:
        features_targets_0_x.append(features[index][0])
        features_targets_0_y.append(features[index][1])
    else:
        features_targets_1_x.append(features[index][0])
        features_targets_1_y.append(features[index][1])

plt.scatter(features_targets_0_x,features_targets_0_y)
plt.scatter(features_targets_1_x,features_targets_1_y)
plt.show()

# 应用径向基函数核的KernelPCA方法
kpca = KernelPCA(kernel='rbf',gamma=15,n_components=1)
features_kpca = kpca.fit_transform(features)

print(features_kpca.shape)