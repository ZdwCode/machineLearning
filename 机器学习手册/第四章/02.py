import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 准备数据
plt.rcParams["font.sans-serif"] = ["Times New Roman"] # 设置字体
plt.rcParams['font.size'] = 16

x_show = [9.0, 10.35, 11.700000000000001, 13.05, 14.4, 15.75, 17.1, 18.45, 19.8, 21.150000000000002, 22.5, 23.85, 25.2]
y_new = [0.2026, 0.204, 0.2058, 0.2081, 0.211, 0.2147, 0.2194, 0.2254, 0.233, 0.2427, 0.255, 0.2706, 0.2904]


plt.text(0.2, 0.48, r"",fontsize=20)
plt.plot(x_show,y_new)
plt.xlabel('height(m)',)
plt.ylabel('Porosity')
plt.show()
