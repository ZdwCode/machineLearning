from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import KFold,cross_val_score


digits = datasets.load_digits()

features = digits.data
target = digits.target

# 创建一个标准化器
standardizer = StandardScaler()

# 创建一个逻辑回归器

logit = LogisticRegression()

# 创建一个含数据标准化和逻辑回归的流水线
pipeline = make_pipeline(standardizer,logit)

# 创建K折交叉验证对象
kf = KFold(n_splits=10,shuffle=True,random_state=1)

# 执行
cv_result = cross_val_score(pipeline,features,target,cv=kf,scoring="accuracy",n_jobs=1)

print(cv_result)