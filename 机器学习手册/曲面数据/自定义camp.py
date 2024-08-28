import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap

# 自定义颜色映射的颜色列表
colors = ['red',
    'blue',
    'green',
    'yellow',
    'black',
    'orange',
    'gray']

# 定义不同的间隔


# 创建 ListedColormap 对象
custom_cmap = ListedColormap(colors, name='custom_cmap', N=7)

# 创建数据
data = pd.read_excel(r'state.xlsx', header=None)
# 将数据转换为二维数组
data = data.values

# 绘制图像，使用不同间隔定义的颜色映射
plt.imshow(data, cmap=custom_cmap, interpolation='nearest')
plt.colorbar()

# 显示图形
plt.show()
