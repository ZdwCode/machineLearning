"""挑出方差大于给定阈值的二值特征"""

from sklearn.feature_selection import VarianceThreshold
features  = [[0,1,0],
             [0,1,1],
             [0,1,0],
             [0,1,1],
             [1,1,0],]

thresholder = VarianceThreshold(threshold=0.75*(1-0.75))
thresholder.fit_transform(features)


"""和数值型特征一样，挑选高信息量的分类特征的方法之一就是查看它们的方差。在二值特征（即伯努利随机变量）中，方差的计算公式如下：

Var(x)=p(1-p)

其中，p是观察值属于第1个分类的概率。通过设置p的值，我们可以删除大部分观察值都属于同一个类别的特征。"""