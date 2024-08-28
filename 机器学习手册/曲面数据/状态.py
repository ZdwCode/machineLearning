import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import pandas as pd
# 创建示例的二维状态数组，不同数字表示不同的状态
plt.rcParams["font.sans-serif"] = ["Arial"]  # 设置字体
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
data = pd.read_excel(r'G:\mogodar_case\case39\i_copy.xlsx', header=None)
# 将数据转换为二维数组
data_array = data.values
state_array = data_array
# 定义状态到颜色的映射
state_colors = {
    1: 'red',
    2: 'blue',
    11: 'green',
    12: 'green',
    20: 'yellow',
    30: 'black',
    40: 'orange',
    50: 'gray'
}

# 获取状态数组的形状
rows, cols = state_array.shape

# 创建一个子图
fig, ax = plt.subplots(figsize=(5, 9))

# 创建多边形列表，用于存储不同状态的区域
polygons = []

for row in range(rows):
    for col in range(cols):
        state = state_array[row, col]
        if state in state_colors:
            color = state_colors[state]
            polygon = Polygon([(col, row), (col + 1, row), (col + 1, row + 1), (col, row + 1)], closed=True,
                              facecolor=color)
            polygons.append(polygon)

# 创建一个多边形集合
p = PatchCollection(polygons, match_original=True,edgecolor=None, linewidths=0)

# 将多边形集合添加到子图中
ax.add_collection(p)

# 设置坐标轴的范围
ax.set_xlim(0, cols+5)
ax.set_ylim(0, rows)
plt.axis('off')

# 添加图例
# state_colors = {
#     'Lumpy zone(coke)': 'red',
#     'Lumpy zone(ore)': 'blue',
#     'Zohesive zone': 'green',
#     'Driping': 'yellow',
#     'Dead man': 'black',
#     'raceway': 'orange',
#     'hearth': 'gray'
# }
# legend_patches = [Polygon([(0, 0), (1, 0), (1, 1), (0, 1)], closed=True, facecolor=color, edgecolor='black', label=f'{state}') for state, color in state_colors.items()]
# legend_patches = legend_patches
# ax.legend(handles=legend_patches,bbox_to_anchor=(1, 1))
# x = []
# for item in np.linspace(-1,1,8):
#     x.append(round(item,1))
# y = []
# for item in np.linspace(0,1,14):
#     y.append(round(item,2))
# y[-1]=1
# plt.xticks(range(0,36,5),x,fontsize=13)
# plt.yticks(range(0,118,9),y,fontsize=13)
# 添加标题和轴标签
# font2 = {'family': 'Arial',
#         'weight': "bold",
#         'size': 20,
#         }
# ax.set_xlabel('radius (r/R)',fontdict=font2)
# ax.set_ylabel('height (r/R)',fontdict=font2)
# ax.set_title('Computational Domain',fontdict=font2)
# 显示图形
plt.show()


"""
data = [[2,1,2,2,1,1,1,1,2,1],
        [2,1,11,1,2,1,2,1,1,1],
        [2,1,1 ,1,2 ,1 ,1 ,1 ,2,1],
        [1,1,1 ,2,2 ,11 ,1 ,1 ,1 ,2],
        [2,2,11 ,2,2 ,1 ,1 ,1 ,2 ,2],
        [1,2,2 ,1 ,1 ,11 ,1 ,2 ,1 ,2],
        [2,1,1 ,2 ,1 ,11 ,1 ,2, 1 ,1],
        [2,1,1 ,11 ,2 ,1 ,1 ,2, 2 ,1],
        [2,2,2 ,11 ,2 ,2 ,1 ,2 ,1 ,2],
        [2,2,1 ,2 ,2 ,2 , 2 ,1, 2,1]]
        """