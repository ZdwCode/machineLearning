import numpy as np
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer

# 创建特征
feature = np.array([['Texas'],
                    ['California'],
                    ['Texas'],
                    ['Delaware'],
                    ['Texas'],])

one_hot = LabelBinarizer()

# 对特征进行one-hot 编码
feature_one_hot = one_hot.fit_transform(feature)
print(feature_one_hot)
print(one_hot.classes_)

# 处理多个分类的特征
multiclass_feature = np.array([['Texas','Florida'],
                    ['California','Alabama'],
                    ['Texas','California'],
                    ['Delaware','Texas'],
                    ['Texas','Delaware'],])
# 创建一个多分类的one-hot编码器
one_hot_multiclass = MultiLabelBinarizer()

# 使用这个编码器
one_hot_multiclass.fit_transform(multiclass_feature)
print(one_hot_multiclass.classes_)
print(one_hot_multiclass.fit_transform(multiclass_feature))