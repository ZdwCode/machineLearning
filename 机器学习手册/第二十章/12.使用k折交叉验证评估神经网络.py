import numpy as np
from keras.preprocessing.text import Tokenizer
from tensorflow.python.keras import models
from tensorflow.python.keras import layers
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from tensorflow.python.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score

np.random.seed(0)
numbers_of_features = 100
features, targets = make_classification(n_samples=10000,
                                        n_features=numbers_of_features,
                                        n_informative=3,
                                        n_classes=2,
                                        weights=[0.5, 0.5],
                                        random_state=0)


# 创建一个函数 返回编译的模型
def create_network():
    network = models.Sequential()

    # 添加使用relu激活函数的全连接层
    network.add(layers.Dense(units=16, activation='relu', input_shape=(numbers_of_features,)))

    network.add(layers.Dense(units=16, activation='relu'))

    network.add(layers.Dense(units=1, activation='sigmoid'))

    # 设计完网络结构之后需要编译
    network.compile(loss='binary_crossentropy',  # 交叉熵损失
                    optimizer='rmsprop',
                    metrics=['accuracy'])
    return network


# 封装模型，好让sk-learn使用
neural_network = KerasClassifier(build_fn=create_network,
                                 epochs=10,
                                 batch_size=100,
                                 verbose=1,)

cross_val_score(neural_network, features, targets, cv=3)
