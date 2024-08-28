# from keras import models
# from keras import layers
from tensorflow.python.keras import models
from tensorflow.python.keras import layers
# 启动神经网络
network = models.Sequential()

# 添加使用relu激活函数的全连接层
network.add(layers.Dense(units=16,activation='relu',input_shape=(10,)))

network.add(layers.Dense(units=16,activation='relu'))

network.add(layers.Dense(units=1,activation='sigmoid'))

# 设计完网络结构之后需要编译
network.compile(loss='binary_crossentropy', # 交叉熵损失
                optimizer='rmsprop',
                metrics=['accuracy'])