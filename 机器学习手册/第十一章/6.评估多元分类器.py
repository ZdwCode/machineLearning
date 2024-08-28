from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
features,targets = make_classification(n_samples=10000,
                                       n_classes=3,
                                       n_features=3,
                                       n_redundant=0,
                                       n_informative=3,
                                       random_state=1)

# 创建逻辑回归器
logit = LogisticRegression()

# 训练
scores = cross_val_score(logit,features,targets,scoring='accuracy')

print(scores)