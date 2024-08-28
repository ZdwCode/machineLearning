import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# 创建示例温度矩阵
data = pd.read_excel(r'G:\mogodar_case\case39\tg.xlsx', header=None)

# 将数据转换为二维数组
data_array = data.values
temperature_matrix = data_array

# 创建热力图
plt.figure(figsize=(3, 8))
heatmap = plt.imshow(temperature_matrix, cmap='coolwarm', aspect='auto', origin='lower', extent=(0, 20, 0, 120))

# 添加等温线
contours = plt.contour(temperature_matrix, colors='black', linewidths=0.5, linestyles='solid', levels=range(100, 2000, 200))
plt.clabel(contours, inline=True, fontsize=8, fmt='%d')

# 添加颜色栏
plt.colorbar(heatmap, label='Temperature (°C)')

# 添加标题和轴标签
plt.title('Temperature Distribution with Contour Lines')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 显示图形
plt.show()
