import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# def normalize_2d_array_to_range(data, new_min=0.2, new_max=0.5):
#     # 计算最小值和最大值
#     min_val = np.min(data)
#     max_val = np.max(data)
#     print(min_val,max_val)
#     # 归一化到指定范围
#     normalized_data = (data - min_val) * (new_max - new_min) / (max_val - min_val) + new_min
#     print((0.18 - min_val) * (new_max - new_min) / (max_val - min_val) + new_min)
#     return normalized_data
#
#
# df = pd.read_excel('G:\mogodar_case\case37\\void.xlsx')
# x = []
# y = []
# z = []
# for i in range(df.shape[0]):
#     x_loc = []
#     z_loc = []
#     for j in range(1,df.shape[1]):
#         # print(df.iloc[i,j],end='\t')
#         if str(df.iloc[i,j])!='nan':
#             x_loc.append(j)
#             z_loc.append(df.iloc[i,j])
#     z.append(z_loc)
#     x.append(x_loc)
#
# for i in range(df.shape[1]):
#     y_loc = []
#     for j in range(1,df.shape[0]):
#         # print(df.iloc[i,j],end='\t')
#         if str(df.iloc[j,i])!='nan':
#             y_loc.append(j)
#     y.append(y_loc)
#
# # z = np.array(z)
# # #z = normalize_2d_array_to_range(z)
# #
# #
# # fig = plt.figure()
# # ax = fig.add_subplot(111, projection='3d')
# #
# # # 绘制三维斜面
# # ax.plot_surface(x, y, z)
# # # 添加标题和标签
# # ax.set_title('三维斜面图')
# # ax.set_xlabel('X轴')
# # ax.set_ylabel('Y轴')
# # ax.set_zlabel('Z轴')
# #
# # # 显示图形
# # plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams["font.sans-serif"] = ["Times New Roman"] # 设置字体
# 读取Excel表格数据
data = pd.read_excel('G:\mogodar_case\case41\\void_show.xlsx')

# 将数据转换为二维数组
data_array = data.values
data_array[40:,7:8] = data_array[40:,7:8]*0.99
data_array[40:,8:9] = data_array[40:,8:9]*0.98
data_array[40:,9:10] = data_array[40:,9:10]*0.97
data_array[40:,10:11] = data_array[40:,10:11]*0.96
data_array[40:,11:12] = data_array[40:,11:12]*0.95
data_array[40:,12:13] = data_array[40:,12:13]*0.94
data_array[40:,13:14] = data_array[40:,13:14]*0.94
data_array[40:,14:] = data_array[40:,14:]*0.93

# 创建横坐标和纵坐标
x = np.arange(data.shape[1])
y = np.arange(data.shape[0])
print(len(y))
# 创建二维网格
X, Y = np.meshgrid(x, y)
print(Y.shape)
# 创建3D图形
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
X = [0.1,0.5,0.8,1.1,1.5,1.8,2.1,2.5,2.8,3.10,3.5,3.8,4.1,4.5,4.8,5.1,5.4,5.7,6.]
Y = [0.11, 0.34, 0.8, 1.03, 1.26, 1.48, 1.71, 1.94, 2.17, 2.4, 2.63, 2.85, 3.08, 3.31, 3.54, 3.77, 3.99, 4.22, 4.45, 4.68, 4.91, 5.14, 5.36, 5.59, 5.82, 6.05, 6.28, 6.51, 6.73, 6.96, 7.19, 7.42, 7.65, 7.88, 8.1, 8.33, 8.56, 8.79, 9.02, 9.25, 9.7, 9.93, 10.16, 10.39, 10.61, 10.84, 11.07, 11.3, 11.53, 11.76, 11.98, 12.21, 12.44, 12.67, 12.9, 13.13, 13.35, 13.58, 13.81, 14.04, 14.27, 14.5, 14.72, 14.95, 15.18, 15.41, 15.64, 15.87, 16.09, 16.32, 16.55, 16.78, 17.01, 17.23, 17.69, 17.92, 18.15, 18.6, 18.83, 19.06, 19.29, 19.52, 19.75, 19.97, 20.2, 20.43, 20.66, 20.89, 21.12, 21.34, 21.57, 21.8, 22.03, 22.26, 22.48, 22.71, 22.94, 23.17, 23.4, 23.63, 23.85, 24.08, 24.31, 24.54, 24.77, 25.0, 25.22, 25.45, 25.68, 25.91, 26.14, 26.37, 26.59, 26.82, 27.05, 27.28]

X, Y = np.meshgrid(X, Y)

print(Y.shape)
ax.plot_surface(X, Y, data_array, cmap='RdYlGn_r')
ax.set_xlabel('Direction of blast furnace radius(m)')
ax.set_ylabel('Direction of blast furnace height(m)')
ax.set_zlabel('porosity')

# 显示图形
plt.show()




