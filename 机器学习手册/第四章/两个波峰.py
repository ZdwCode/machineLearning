import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 准备数据
plt.rcParams["font.sans-serif"] = ["SimHei"] # 设置字体

x = range(0,21,1)
x_new = range(0,21,1)
print(len(x))
y = np.array([0.33,0.35,0.35,0.18,0.18,0.40,0.40,0.22,0.22,0.50,0.5,0.20,0.2,0.35,0.35,0.40,0.40,0.35,0.34,0.50,0.40])
print(len(y))
z1 = np.polyfit(x, y, 7)
print()
y_new = np.poly1d(z1)
print(y_new)
y_new = np.polyval(z1,x_new)
ax = plt.gca()
ax.plot(x_new,y_new)
ax.scatter(x_new,y_new,s=10)
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