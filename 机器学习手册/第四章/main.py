import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 准备数据
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
x=range(0,21,1)
# x = np.array([22,19,17,15,13,11,9,7,5,3,0])
y = np.array([0.356,0.35,0.321,0.341,0.343,0.286,0.317,0.34,0.308])
# y = np.array([0.410,0.40,0.360,0.355,0.35,0.348,0.34,0.33,0.32]) # 平滑减小
# y = np.array([0.37,0.38,0.35,0.348,0.365,0.377,0.348,0.33,0.32]) # 两个波峰
# y = np.linspace(0.18, 0.50, 21, retstep=True)
# y = np.array([0.18, 0.196, 0.212, 0.22799999999999998, 0.244, 0.26, 0.276, 0.292, 0.308, 0.324, 0.33999999999999997, 0.356, 0.372, 0.388, 0.404, 0.42, 0.436, 0.452, 0.468, 0.484, 0.5])
# my_y = []
# for item in y[0]:
#     my_y.append(item)
# print(my_y)
print(len(x),len(y))
print(y[0])
z1 = np.polyfit(x, y, 2)
y_new = np.poly1d(z1)
print(y_new)
y_new = np.polyval(z1,x)
plt.plot(x,y_new)
plt.scatter(x,y)
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