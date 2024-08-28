import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from matplotlib.colors import ListedColormap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches

# 创建数据
x = np.linspace(-18, 18, 36)
y = np.linspace(0, 116, 116)
x, y = np.meshgrid(x, y)
print(x.shape)
print(y.shape)
data_1 = pd.read_excel(r'G:\mogodar_case\case47\void_show_copy.xlsx', header=None)
# data_2 = pd.read_excel(r'G:\mogodar_case\case45\void_show_copy.xlsx', header=None)
# data_3 = pd.read_excel(r'G:\mogodar_case\case47\void_show_copy.xlsx', header=None)
print(data_1.shape)
# 将数据转换为二维数组
# data_array = data.values
z_1 = data_1.values  # Z轴的高度为 sin(sqrt(x^2 + y^2))
print(type(z_1))
# z_2 = data_2.values  # Z轴的高度为 sin(sqrt(x^2 + y^2))
# z_3 = data_3.values*0.85  # Z轴的高度为 sin(sqrt(x^2 + y^2))
data2 = pd.read_excel(r'G:\mogodar_case\case43\tg_copy.xlsx', header=None)
z_i = data2.values
# 创建3D图形
camps = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
camps = ['RdYlGn']
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
mycmap = ListedColormap(colors, name='custom_cmap', N=7)
for camp in camps:
    print(camp)
    # 绘制曲面

    fig = plt.figure(figsize=(12,9))
    ax = fig.add_subplot(111, projection='3d')
    surface_1 = ax.plot_surface(x, y, z_1, cmap=camp, alpha=0.8, label='Surface')
    # surface_2 = ax.plot_surface(x, y, z_2, cmap=camp, alpha=0.8, label='Surface')
    # surface_3 = ax.plot_surface(x, y, z_3, cmap=camp, alpha=0.8, label='Surface')
    ax.set_zlim(-0.2, 0.6)
    # ax.tick_params(pad=5)
    # 在XOY平面上绘制圆形
    ax.contourf(x, y, z_i,zdir='z', offset=-.2,cmap=mycmap)  #生成z方向投影，投到x-y平面
    # 将多边形集合添加到子图中
    # ax.add_collection(p)
    # cax = fig.add_axes([0.94, 0.1, 0.02, ax.get_position().height])
    # plt.colorbar(surface_1, ax=ax,fraction=0.01, cax=cax,)
    font = {'family': 'serif',
            'color': 'darkred',
            'weight': 'normal',
            'size': 16,
            }
    # plt.colorbar(surface_2, ax=ax, fraction=0.02, cax=cax)
    # plt.colorbar(surface_3, ax=ax, fraction=0.02, cax=cax)
    # 添加标签和标题
    x = []
    for item in np.linspace(-1, 1, 8):
        x.append(round(item, 1))
    y = []
    for item in np.linspace(0, 1, 11):
        y.append(round(item, 2))
    y[-1] = 1
    ax.set_xticks(range(-18, 18, 5), x, fontsize=25, )
    ax.set_yticks(range(0, 118, 11), y, fontsize=25, rotation=-15, )
    ax.set_zticks([0,0.1,0.2,0.3,0.4,0.5])
    ax.tick_params(axis='z', labelsize=25)
    font2 = {'family': 'Arial',
             'weight': "bold",
             'size': 30,
             }
    ax.set_xlabel('radius (r/R)',fontdict=font2,labelpad=20)
    ax.set_ylabel('height (h/H)',fontdict=font2,labelpad=20)
    ax.set_zlabel('Porosity',fontdict=font2,labelpad=17)
    plt.subplots_adjust(left=0, right=1, top=0.96, bottom=0.15)
    # 显示图形
    plt.show()
