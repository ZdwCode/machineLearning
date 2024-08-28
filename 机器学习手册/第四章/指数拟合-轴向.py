import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 准备数据
plt.rcParams["font.sans-serif"] = ["Arial"] # 设置字体
plt.rcParams['font.size'] = 16

x = [9,28]
x_new = range(9,28,1)
y = []
for i in range(9,28):
    y.append(0.00009 * 2.71 **(0.3*i) + 0.2)
# plt.text(10, 0.48, r"Porosity=0.00009e^0.3h+0.2",fontsize=20)
plt.plot(x_new,y,color='#7cd6cf',linewidth=3.0)
font2 = {'family': 'Arial',
        'weight': "bold",
        'size': 20,
        }
plt.xlabel('height(m)',fontdict=font2)
plt.ylabel('Porosity',fontdict=font2)
plt.tick_params(axis="both", labelsize=15,width=4,length=6)
bwith = 3  # 边框宽度设置为2
TK = plt.gca()  # 获取边框
TK.spines['bottom'].set_linewidth(bwith)  # 图框下边
TK.spines['left'].set_linewidth(bwith)  # 图框左边
TK.spines['top'].set_linewidth(bwith)  # 图框上边
TK.spines['right'].set_linewidth(bwith)  # 图框右边
plt.subplots_adjust(left=0.135, right=0.985, top=0.973, bottom=0.135)
plt.grid(ls=':',
         color='#9192ab')  # 设置网格，颜色为蓝色
plt.show()
