import numpy as np
from keras.datasets import reuters
from keras.preprocessing.text import Tokenizer
from tensorflow.python.keras import models
from tensorflow.python.keras import layers
from keras.utils.np_utils import to_categorical
np.random.seed(0)

# 设定想要的特征数量
number_of_features = 5000

# 从影评数据中加载数据
data = reuters.load_data(nb_words=number_of_features)
(data_train,target_train),(data_test,target_test) = data
print(target_test)
# 将影评数据转化为one-hot编码
tokenizer = Tokenizer(nb_words=number_of_features)
features_train = tokenizer.sequences_to_matrix(data_train,mode='binary')
features_test = tokenizer.sequences_to_matrix(data_test,mode='binary')
# print(features_train[0])
# 把one-hot编码的特征向量转化成特征举证
print(target_train)
target_train = to_categorical(target_train)
print(target_train)
target_test = to_categorical(target_test)
network = models.Sequential()

# 添加使用relu激活函数的全连接层
network.add(layers.Dense(units=100,activation='relu',input_shape=(number_of_features,)))

network.add(layers.Dense(units=100,activation='relu'))

network.add(layers.Dense(units=46,activation='softmax'))

# 设计完网络结构之后需要编译
network.compile(loss='categorical_crossentropy', # 交叉熵损失
                optimizer='rmsprop',
                metrics=['accuracy'])

# 训练网络
history = network.fit(features_train,target_train,
            epochs=3,
            verbose=1,
            batch_size=100,
            validation_data=(features_test,target_test))