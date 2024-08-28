from sklearn.linear_model import Ridge,RidgeCV
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import validation_curve
import numpy as np
boston = load_boston()
feature = boston.data[:,0:2]
target = boston.target
# 特征标准化
scaler = StandardScaler()
feature_standardized = scaler.fit_transform(feature)
# 创建岭回归
regression = Ridge(alpha=0.5)

model = regression.fit(feature_standardized,target)
# regre_cv = RidgeCV(alphas=[0.1,1.0,10.0])
# model_cv = regre_cv.fit(feature_standardized,target)
# print(model_cv.alpha_)


param_range = [0.1,1.0,10.0]
train_scores,test_scores = validation_curve(
    # 分类器
    RidgeCV(),
    # 特征
    feature_standardized,
    target,
    param_name='alphas',
    param_range=param_range,
    cv=3,
    scoring='accuracy',
    n_jobs=1
)
print(train_scores)