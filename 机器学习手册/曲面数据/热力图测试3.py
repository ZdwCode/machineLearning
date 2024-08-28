import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
import pandas as pd
# 创建示例状态矩阵，假设有5种不同的状态
data = pd.read_excel(r'G:\mogodar_case\case39\i.xlsx', header=None)
# 将数据转换为二维数组
data_array = data.values
status_matrix = data_array  # 假设有5种状态

# 创建热力图，表示不同状态
plt.figure(figsize=(8, 8))
plt.imshow(status_matrix, cmap='coolwarm', extent=(0, 20, 0, 20), origin='lower')

# 找到相同状态的点并圈出来
for state in range(1, 6):
    mask = (status_matrix == state)
    labeled, num_features = ndimage.label(mask)
    for i in range(1, num_features + 1):
        labeled_mask = (labeled == i)
        y_positions, x_positions = np.where(labeled_mask)
        if len(x_positions) > 0:
            min_x, max_x, min_y, max_y = min(x_positions), max(x_positions), min(y_positions), max(y_positions)
            plt.plot([min_x, max_x, max_x, min_x, min_x], [min_y, min_y, max_y, max_y, min_y], 'r-', linewidth=2)

# 添加标题和轴标签
plt.title('Grouped Points of Same States')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 显示图形
plt.show()
