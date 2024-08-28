import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 准备数据
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体 # 设置字体
plt.rcParams['font.size'] = 16

x_show = [0.0, 0.6, 1.2, 1.7999999999999998, 2.4, 3.0, 3.5999999999999996, 4.2, 4.8, 5.3999999999999995]
y_new=[0.2052, 0.2071, 0.210, 0.2147, 0.2214, 0.2314, 0.2475, 0.2718, 0.3072, 0.3588]

plt.text(0.2, 0.48, r"",fontsize=20)
plt.plot(x_show,y_new[0:19])
plt.xlabel('Radius(m)',)
plt.ylabel('Porosity')
plt.subplots_adjust(left=0.135, right=0.914, top=0.973, bottom=0.118)
plt.show()
