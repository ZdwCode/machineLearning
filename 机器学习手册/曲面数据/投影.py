import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 创建数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 创建三维图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三维曲面
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)

# 添加正方形在 xy 平面
square = np.array([[2, 2, 0],
                   [2, -2, 0],
                   [-2, -2, 0],
                   [-2, 2, 0]])
verts = [list(zip(square[:, 0], square[:, 1], square[:, 2]))]
ax.add_collection3d(Poly3DCollection(verts, facecolors='gray', linewidths=1, edgecolors='black', alpha=0.5))

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 设置视角
ax.view_init(elev=20, azim=30)

# 显示图形
plt.show()
