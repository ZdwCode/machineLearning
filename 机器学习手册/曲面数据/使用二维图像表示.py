import matplotlib
import matplotlib.colors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# 读取Excel表格数据
from PIL import Image

data = pd.read_excel(r'G:\mogodar_case\case43\void_show.xlsx', header=None)

# 将数据转换为二维数组
data_array = data.values
# data_array[40:,:] = data_array[40:,:]*1.1 # 43
# [40:,:] = data_array[40:,:]*0.85 47
mylist_y = []
mylist_x = []
for myindex in range(40,118):
    if (myindex-40)%6 == 0:
        mylist_y.append(data_array[myindex,0])
        mylist_x.append(myindex*0.225)
print(mylist_x)
print(mylist_y)

mylist_y = []
mylist_x = []
for myindex in range(0,20):
    if myindex%2 == 0:
        mylist_y.append(data_array[50,myindex])
        mylist_x.append(myindex*0.3)
print(mylist_x)
print(mylist_y)

# data_array.to_excel(r'G:\mogodar_case\case43\void_show_new.xlsx', header=None)
#result = pd.DataFrame(data_array)
#result.to_excel(r'G:\mogodar_case\case43\void_show_new.xlsx', header=None)
#print(type(result))
# 创建横坐标和纵坐标
x = np.arange(data.shape[1])
y = np.arange(data.shape[0])

# 创建图形，并设置图形大小
fig, ax = plt.subplots(figsize=(8, 12))
# ax.text(14, 115, r"Porosity = 0.05 r + 0.2",fontsize=8);
xticklabels = [0.1, 0.5, 0.8, 1.1, 1.5, 1.8, 2.1, 2.5, 2.8, 3.10, 3.5, 3.8, 4.1, 4.5, 4.8, 5.1, 5.4, 5.7, 6.]
# [0.0, 0.08, 0.15, 0.23, 0.31, 0.38, 0.46, 0.54, 0.62, 0.69, 0.77, 0.85, 0.92, 1]
yticklabels = [0.0, '', '', '', '', '', '', '', '',  '',0.08,  '','', '', '','', '', '', '','', 0.15,  '','', '','',  '', '', '','', '',  0.23, '','',
               '', '', '', '', '', '', '',0.31, '', '', '', '', '', '',  '', '','', 0.38,  '','', '', '', '', '','', 0.46,  '','', '','', '',  '', '', '', 0.54,
               '', '', '', '', '', '', '',0.62, '', '', '', '',  '', '', '', 0.69, '',  '', '', '', '', '', '', 0.77, '', '', '', '', '', '', '', '',
                0.85, '', '', '', '',  '', '',  0.92,'', '', '', '', '',  '',  '', 1]
# 绘制热图
# im = ax.imshow(data_array, cmap='viridis')
sns.set(font_scale=0.5)
cmap = sns.heatmap(data_array, vmax=1.0, vmin=0, cmap='RdYlGn_r', annot=True, xticklabels=xticklabels, yticklabels=yticklabels,
            linewidths=.6, cbar_kws={"shrink": .65}, annot_kws={'color': 'black'})
# 添加颜色条
cbar = cmap.collections[0].colorbar
# cbar = plt.colorbar(im)
cbar.ax.tick_params(labelsize=15)
ax.tick_params(labelsize=8)
fontdict = {'fontsize': 15, }
# img = Image.open(r'G:\mogodar_case\图像\径向\指数函数分布.png')
# img = img.resize((int(img.width * 0.4), int(img.height * 0.4)))
# 设置坐标轴标签
sns.set(font_scale=1)
font2 = {'family': 'Arial',
        'weight': "bold",
        'size': 20,
        }
ax.set_xlabel('radius(r/R)',fontdict=font2)
ax.set_ylabel('height(r/R)',fontdict=font2)
ax.set_title('Porosity',fontdict=font2)
ax.tick_params(axis='x', labelsize=15,width=2,length=6)
ax.tick_params(axis='y', labelsize=15,length=6,bottom=0,top=117)
ax.invert_yaxis()
# 显示图形
# plt.figimage(img, xo=480, yo=850)
plt.subplots_adjust(left=0.085, right=1.0, top=0.965, bottom=0.065)
plt.show()
