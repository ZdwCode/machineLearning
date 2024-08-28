import numpy as np
from keras.preprocessing.text import Tokenizer
from tensorflow.python.keras import models
from tensorflow.python.keras import layers
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

np.random.seed(0)

features, targets = make_regression(n_samples=10000,
                                    n_features=3,
                                    n_informative=3,
                                    n_targets=2,
                                    random_state=0)
print(features,targets)
# 划分数据集和测试集合
features_train,features_test,target_train,target_test = \
    train_test_split(features,targets,test_size=0.33,random_state=0) # 特征 特征 目标 目标
#
network = models.Sequential()

# 添加使用relu激活函数的全连接层
network.add(layers.Dense(units=32,activation='relu',input_shape=(features_train.shape[1],)))

network.add(layers.Dense(units=32,activation='relu'))

network.add(layers.Dense(units=2))

# 设计完网络结构之后需要编译
network.compile(loss='mse', #
                optimizer='RMSprop',
                metrics=['mse'])

# 训练网络
history = network.fit(features_train,target_train,
            epochs=10,
            verbose=1,
            batch_size=100,
            validation_data=(features_test,target_test))
