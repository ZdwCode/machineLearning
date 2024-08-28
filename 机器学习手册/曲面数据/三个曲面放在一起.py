import math

import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from mpl_toolkits.mplot3d import Axes3D

class Linear:
    def normalize_2d_array_to_range(self,data, new_min=0.2, new_max=0.5):
        # 计算最小值和最大值
        min_val = np.min(data)
        max_val = np.max(data)
        # 归一化到指定范围
        normalized_data = (data - min_val) * (new_max - new_min) / (max_val - min_val) + new_min
        return normalized_data

    def getZ(self):
        x = np.linspace(0, 20, 20)  # X轴数据范围
        y = np.linspace(0, 90, 90)  # Y轴数据范围
        x, y = np.meshgrid(x, y)  # 创建网格
        z = 0.04 * x + 0.1 * (90-y)  # 斜面方程:z = 2x + 3y，你可以根据需要调整斜率和截距
        z = self.normalize_2d_array_to_range(z)
        return z


class Exponential:
    def normalize_2d_array_to_range(self,data, new_min=0.2, new_max=0.5):
        # 计算最小值和最大值
        min_val = np.min(data)
        max_val = np.max(data)
        # 归一化到指定范围
        normalized_data = (data - min_val) * (new_max - new_min) / (max_val - min_val) + new_min

        return normalized_data

    def getZ(self):
        x = np.linspace(0, 20, 20)  # X轴数据范围
        y = np.linspace(0, 90, 90)  # Y轴数据范围
        x, y = np.meshgrid(x, y)  # 创建网格
        z = np.exp(0.1 * x) + np.exp(0.04 * (90 - y))  # 斜面方程:z = 2x + 3y，你可以根据需要调整斜率和截距
        z = self.normalize_2d_array_to_range(z)
        return z


class Log:
    def normalize_2d_array_to_range(self,data, new_min=0.2, new_max=0.5):
        # 计算最小值和最大值
        min_val = np.min(data)
        max_val = np.max(data)
        print(min_val, max_val)
        # 归一化到指定范围
        normalized_data = (data - min_val) * (new_max - new_min) / (max_val - min_val) + new_min

        return normalized_data

    def getZ(self):
        x = np.linspace(1, 20, 20)  # X轴数据范围
        y = np.linspace(1, 90, 90)  # Y轴数据范围
        x, y = np.meshgrid(x, y)  # 创建网格
        z = np.log(x) + np.log((91 - y))  # 斜面方程:z = 2x + 3y，你可以根据需要调整斜率和截距

        z = self.normalize_2d_array_to_range(z)
        return z


plt.rcParams["font.sans-serif"] = ["SimHei"] # 设置字体
# 生成数据
x = np.linspace(1, 20, 20)  # X轴数据范围
y = np.linspace(1, 90, 90)  # Y轴数据范围
x, y = np.meshgrid(x, y)  # 创建网格

z1 = Linear().getZ()
z2 = Exponential().getZ()
z3 = Log().getZ()

# 创建3D图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三维斜面
ax.plot_surface(x, y, z1)
ax.plot_surface(x, y, z2)
ax.plot_surface(x, y, z3)

# 添加标题和标签
ax.set_title('三维斜面图')
ax.set_xlabel('X轴')
ax.set_ylabel('Y轴')
ax.set_zlabel('Z轴')

# 显示图形
plt.show()

