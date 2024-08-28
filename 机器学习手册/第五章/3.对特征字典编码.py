"""使用DictVectorizer将字典转化成一个特征矩阵"""
from sklearn.feature_extraction import DictVectorizer


# 创建一个字典
data_dict = [{"red":2,"blue":4},
             {"red":4,"blue":3},
             {"red":1,"yellow":2},
             {"red":2,"yellow":2}]

# 创建字典向量化器
dictVectorizer = DictVectorizer(sparse=False)

features = dictVectorizer.fit_transform(data_dict)

print(features)
print(dictVectorizer.get_feature_names_out())