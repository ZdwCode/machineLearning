"""
准确率=（真阳+真阴）/(真阳+真阴+假阳+假阴)  通俗点就是预测正确的概率
精准度=真阳/（真阳+假阳)
召回率=真阳/(真阳+假阴)
F1分数=2*(精准度*召回率)/(精准度+召回率)
"""
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
X,y= make_classification(n_samples=1000,n_features=3,n_informative=3,n_redundant=0,n_classes=2,random_state=1)

# 创建逻辑回归对象
logit = LogisticRegression()

# 使用准确率对模型进行交叉验证
score = cross_val_score(logit,X,y,scoring='accuracy')
print(score)
# 使用精准度对模型进行交叉验证
score = cross_val_score(logit,X,y,scoring='precision')
print(score)
# 使用准确率对模型进行交叉验证
score = cross_val_score(logit,X,y,scoring='recall')
print(score)
# 使用f1分数对模型进行交叉验证
score = cross_val_score(logit,X,y,scoring='f1')
print(score)