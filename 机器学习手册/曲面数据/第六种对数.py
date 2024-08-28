import math

import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from mpl_toolkits.mplot3d import Axes3D

def normalize_2d_array_to_range(data, new_min=0.2, new_max=0.55):
    # 计算最小值和最大值
    min_val = np.min(data)
    max_val = np.max(data)
    print(min_val,max_val)
    # 归一化到指定范围
    normalized_data = (data - min_val) * (new_max - new_min) / (max_val - min_val) + new_min

    return normalized_data


plt.rcParams["font.sans-serif"] = ["SimHei"] # 设置字体
# 生成数据
x = np.linspace(1, 20, 20)  # X轴数据范围
y = np.linspace(1, 90, 80)  # Y轴数据范围
x, y = np.meshgrid(x, y)  # 创建网格
z = np.log(0.1*x) + np.log(0.04*(91-y))   # 斜面方程:z = 2x + 3y，你可以根据需要调整斜率和截距
print(z)
z = normalize_2d_array_to_range(z)
print(z)
# 创建3D图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三维斜面
ax.plot_surface(x, y, z)

# 添加标题和标签
ax.set_xlim(0,18)
ax.set_title('三维斜面图')
ax.set_xlabel('X轴')
ax.set_ylabel('Y轴')
ax.set_zlabel('Z轴')

# 显示图形
plt.show()
