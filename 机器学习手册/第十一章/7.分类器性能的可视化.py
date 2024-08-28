"""使用混淆矩阵来比较预测分类和真实分类"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
iris = datasets.load_iris()

features,targets = iris.data,iris.target

class_name = iris.target_names

features_train,features_test,targets_train,targets_test = train_test_split(features,targets,random_state=1)

# 创建逻辑回归
logit = LogisticRegression()

# 训练模型
logit.fit(features_train,targets_train)

# 预测结果
predicts = logit.predict(features_test)
print(targets_test)
print(predicts)
print(len(predicts))
# 创建混淆矩阵
matrix = confusion_matrix(targets_test,predicts)

print(matrix)

# 可视化混淆矩阵
dataframe = pd.DataFrame(matrix,index=class_name,columns=class_name)

# 使用热力图
sns.heatmap(dataframe,annot=True,cbar=None,cmap='Blues')
plt.title('Confusion Matrix')
plt.show()