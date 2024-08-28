import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 准备数据
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
x=range(0,21,1)
y = np.array([0.18, 0.185, 0.186, 0.190, 0.198, 0.21, 0.222, 0.233, 0.244, 0.255, 0.28, 0.31, 0.316, 0.33, 0.37, 0.436, 0.455, 0.479, 0.499, 0.5, 0.5])
z1 = np.polyfit(x, y, 2)
print()
y_new = np.poly1d(z1)
print(y_new)
y_new = np.polyval(z1,x)
ax = plt.gca()
ax.plot(x,y_new)
ax.scatter(x,y_new,s=10)
ax.scatter(x,y,s=10)
ax.set_xlabel('高炉距离炉中心距离')
ax.set_ylabel('孔隙率')
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
#plt.legend()
plt.show()
# x_new = np.arange(40,120)
# y_new = np.polyval(z1,x_new)
# print(y_new)
# # plt.plot(y)
# ax = plt.gca()
# x_new = range(120,40,-1)
# #ax.plot(y_new-0.04,x_new,label='-0.04')
# #ax.plot(y_new-0.02,x_new,label='-0.02')
# ax.plot(y_new,x_new,label='0.00')
# #ax.plot(y_new+0.02,x_new,label='+0.02')
# #ax.plot(y_new+0.04,x_new,label='+0.04')
# #ax.xaxis.set_ticks_position('top')
# #ax.invert_yaxis()  #y轴反向
# #ax.XAxisLocation = 'top'
# ax.set_xlabel('孔隙率')
# ax.set_ylabel('高炉距离炉顶距离')
# plt.legend()
# plt.show()
# temp = 70
# User_Porosity = 7.336E-07 * temp**3 - 7.854E-05 * temp ** 2 + 0.0002233 * temp + 0.4121
#
# print(User_Porosity)
# print(80**5)