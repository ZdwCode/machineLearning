import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_erosion
import pandas as pd
from scipy import ndimage
# 创建示例温度矩阵
plt.rcParams["font.sans-serif"] = ["Arial"]  # 设置字体
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
path = r'G:\mogodar_case\case43\tg_copy.xlsx'
data = pd.read_excel(path, header=None)
# 将数据转换为二维数组
data_array = data.values
temperature_matrix = data_array


# 创建热力图
plt.figure(figsize=(6, 9))
heatmap = plt.imshow(temperature_matrix, cmap='RdYlGn_r', aspect='auto', origin='lower', interpolation='bilinear')

# 添加等温线
contours = plt.contour(temperature_matrix, colors='black', linewidths=0.5, linestyles='solid',levels=[400,800,1200,1600,1800])
plt.clabel(contours, inline=True, fontsize=14, fmt='%d',inline_spacing=5)

plt.colorbar(heatmap,fraction=0.08)

# 添加标题和轴标签
ax = plt.gca()
plt.text(1.03,0.97,'Gas tempe\n rature (°C)',transform=ax.transAxes,fontsize=12)
x = []
for item in np.linspace(-1,1,5):
    x.append(round(item,1))
y = []
for item in np.linspace(0,1,14):
    y.append(round(item,2))

y[-1]=1
print(y)
plt.xticks(range(0,36,8),x,fontsize=25)
plt.yticks(range(0,118,9),y,fontsize=25)
font2 = {'family': 'Arial',
             'weight': 'bold',
             'size': 30,
             }
plt.xlabel('radius (r/R)',fontdict=font2)
plt.ylabel('height (h/H)',fontdict=font2)
plt.ylim(0,117)
#top=0.98,
# bottom=0.065,
# left=0.215,
# right=0.85,
# hspace=0.2,
# wspace=0.2
# 显示图例
plt.subplots_adjust(left=0.215, right=0.875, top=0.98, bottom=0.1)
save_path = r'G:\poststudy\2024-04\论文修改\温度\case_9.png'
plt.savefig(save_path)
# 显示图形
# plt.show()
