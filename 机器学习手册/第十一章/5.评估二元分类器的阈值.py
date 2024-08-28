"""
ROC曲线会对每一个概率阈值（即用来区分样本属于正类或负类的概率值）
比较其真阳性和假阳性的比例。通过绘制ROC曲线，我们可以观察模型的性能。
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve,roc_auc_score
import matplotlib.pyplot as plt
features,targets = make_classification(n_samples=10000,n_features=10,n_classes=2,n_informative=3,random_state=3)

features_train,features_test,targets_train,targets_test = train_test_split(features,targets,random_state=1)

logit = LogisticRegression()

logit.fit(features_train,targets_train)


# 获取预测的概率

target_probabilities = logit.predict_proba(features_test)[:,1]

# 计算真阳性和假阳性的概率
false_positive_rate,true_positive_rate,threshold = roc_curve(targets_test,target_probabilities)

# 画出roc曲线
plt.plot(false_positive_rate,true_positive_rate)
plt.plot([0,1],ls='--')
plt.plot([0,0],[1,0],c='.7'),plt.plot([1,1],c='.7')
plt.show()
