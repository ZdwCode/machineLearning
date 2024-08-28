import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
#
# 准备数据
# plt.rcParams["font.sans-serif"] = ["SimHei"] # 设置字体
#
# x = [0.1,6]
# x_new = range(0,7,1)
# y = []
# for i in range(0,7):
#
#     y.append(0.00075 * 2.71 ** i + 0.2)
# print(2.71**0.31,)
# plt.text(0.2, 0.48, r"Porosity=0.00075e^r+0.2",fontsize=20)
# plt.plot(x_new,y)
# plt.xlabel('Direction of blast furnace radius')
# plt.ylabel('Porosity')
# plt.show()

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 准备数据
plt.rcParams["font.sans-serif"] = ["Arial"] # 设置字体
plt.rcParams['font.size'] = 16
x = [0,2,3,4,6]
x_new = [0,0.5,0.8,1.1,1.5,1.8,2.1,2.5,2.8,3.10, 3.5,3.8,4.1,4.5,4.8, 5.1,5.4,5.7,6.]
x_newexp = np.exp(x_new)
y = [0.,0.25,0.35,0.4,0.5]
xexp = np.exp(x)
z1 = np.polyfit(xexp, y, 1)
y_new = np.poly1d(z1)
print(y_new)
x_show = [0,0.5,0.8,1.1,1.5,1.8,2.1,2.5,2.8,3.10, 3.5,3.8,4.1,4.5,4.8, 5.1,5.4,5.7,6.]
y_new = np.polyval(z1,x_newexp )
print(y_new)
plt.plot(x_show,y_new,color='#7cd6cf',linewidth=3.0)
font2 = {'family': 'Arial',
        'weight': "bold",
        'size': 20,
        }
plt.xlabel('radius(m)',fontdict=font2)
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
