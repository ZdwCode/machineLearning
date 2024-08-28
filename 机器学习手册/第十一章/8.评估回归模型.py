"""使用均方误差和R方来评估回归模型"""
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

features,targets = make_regression(n_samples=100,n_features=3,n_informative=3,n_targets=1,
                                   noise=50,coef=False,random_state=1)

# 创建线性回归对象
ols = LinearRegression()

# 使用均方误差评估
score = cross_val_score(ols,features,targets,scoring='neg_mean_squared_error')
print(score)
# 使用R方评估
score = cross_val_score(ols,features,targets,scoring='r2')
print(score)

