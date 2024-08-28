import numpy as np
from tensorflow.python.keras.datasets import imdb
from keras.preprocessing.text import Tokenizer
from tensorflow.python.keras import models
from tensorflow.python.keras import layers,regularizers
import matplotlib.pyplot as plt
np.random.seed(0)

# 设定想要的特征数量
number_of_features = 1000

# 从影评数据中加载数据
(data_train,target_train),(data_test,target_test) = imdb.load_data(num_words=number_of_features)
print(target_test)
# 将影评数据转化为one-hot编码
tokenizer = Tokenizer(nb_words=number_of_features)
features_train = tokenizer.sequences_to_matrix(data_train,mode='binary')
features_test = tokenizer.sequences_to_matrix(data_test,mode='binary')
# print(features_train[0])

network = models.Sequential()

# 添加使用relu激活函数的全连接层
network.add(layers.Dense(units=16,activation='relu',kernel_regularizer=regularizers.l2(0.01),input_shape=(number_of_features,)))

network.add(layers.Dense(units=16,activation='relu',kernel_regularizer=regularizers.l2(0.01)))

network.add(layers.Dense(units=1,activation='sigmoid'))

# 设计完网络结构之后需要编译
network.compile(loss='binary_crossentropy', # 交叉熵损失
                optimizer='rmsprop',
                metrics=['accuracy'])

# 训练网络
history = network.fit(features_train,target_train,
            epochs=20,
            verbose=1,
            batch_size=100,
            validation_data=(features_test,target_test))


# 获取训练集和测试集的损失值
train_loss = history.history['loss'] # acc val_acc
test_loss = history.history['val_loss']
# w为每个epoch创建编号
epoch_count = range(1,len(train_loss)+1)
# 画出损失的历史数值
plt.plot(epoch_count,train_loss,'r--')
plt.plot(epoch_count,test_loss,'b-')
plt.show()