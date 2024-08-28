# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.ndimage import binary_erosion
# import pandas as pd
# from scipy import ndimage
# # 创建示例温度矩阵
# plt.rcParams["font.sans-serif"] = ["Arial"]  # 设置字体
# plt.rcParams["font.weight"] = "bold"
# plt.rcParams["axes.labelweight"] = "bold"
# data = pd.read_excel(r'G:\mogodar_case\case39\i.xlsx', header=None)
# # 将数据转换为二维数组
# data_array = data.values
# temperature_matrix = data_array
#
#
# # 创建热力图
# plt.figure(figsize=(3, 8))
# heatmap = plt.imshow(temperature_matrix,vmax=5, vmin=0,cmap='coolwarm', aspect='auto', origin='lower', extent=(0, 20, 0, 117),)
#
# # 添加等温线
#
#
# # 绘制黑色边缘线
# for i in range(117):
#     for j in range(19):
#         if np.isnan(temperature_matrix[i, j]) and np.isnan(temperature_matrix[i, j-1]) == False:
#             plt.plot([j+0.8,j+0.8],[i, i+1], color='black',ls='-', linewidth=2)
#         if np.isnan(temperature_matrix[i, j]) == False and j==18:
#             print(i,j)
#             plt.plot([j+1.8, j+1.8], [i, i+0.5], color='black', ls='-', linewidth=2)
#
# for i in range(116):
#     for j in range(19):
#         if np.isnan(temperature_matrix[i, j]) and np.isnan(temperature_matrix[i-1, j]) == False:
#             plt.plot([j+1,j+1.7],[i, i], color='black',ls='-', linewidth=2)
#         if np.isnan(temperature_matrix[i, j]) and np.isnan(temperature_matrix[i+1, j]) == False:
#             plt.plot([j+1,j+1.7],[i+1, i+1], color='black',ls='-', linewidth=2)
# # 添加颜色栏
# plt.colorbar(heatmap)
#
# # 添加标题和轴标签
# ax = plt.gca()
# plt.text(1,0.95,'Temperat\n ure (°C)',transform=ax.transAxes,fontsize=12)
# x = []
# for item in np.linspace(0,6,6):
#     x.append(round(item,2))
# y = []
# for item in np.linspace(0,27,14):
#     y.append(round(item,2))
# y[-1]=27.28
# plt.xticks(range(0,24,4),x)
# plt.yticks(range(0,118,9),y)
# plt.xlabel('radius(m)')
# plt.ylabel('height(m)')
# plt.ylim(0,117)
# # 显示图例
# plt.subplots_adjust(left=0.23, right=0.85, top=0.98, bottom=0.06)
# # 显示图形
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# 创建一个示例的二维数组，你需要替换成你的数据
data = np.array([[0, 0, 1, 1],
                 [0, 2, 2, 1],
                 [0, 2, 2, 2],
                 [3, 3, 3, 3]])

# 获取不同状态的唯一值
unique_states = np.unique(data)

# 创建一个颜色映射，将不同状态映射到不同的颜色
normalize = Normalize(vmin=0, vmax=len(unique_states)-1)
colors = plt.cm.viridis(normalize(unique_states))

# 创建一个图形对象
fig, ax = plt.subplots()

# 遍历数组并根据不同状态绘制矩形
for i, state in enumerate(unique_states):
    state_data = data == state
    ax.imshow(state_data, cmap=colors[i], interpolation='none', extent=[0, data.shape[1], 0, data.shape[0]])

# 隐藏坐标轴
ax.axis('off')

plt.show()
