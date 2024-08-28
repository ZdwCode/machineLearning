from sympy import symbols, Eq, log, solve

# 定义符号变量
a, b = symbols('a b')

# 构建方程
eq = Eq(a * log(3) + b, 0.5736)

# 解方程
solution = solve(eq, (a, b))

# 得到解的值
a_value = solution[a]
b_value = solution[b]

# 构建中心对称的函数
def symmetric_function(x):
    return a_value * log(3 - (x - 3)) + b_value

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 10, 100)
y_original = 0.073 * np.log(x) + 0.37
y_symmetric = [symmetric_function(xi) for xi in x]

plt.plot(x, y_original, label='Original Function (f(x) = 0.073 * log(x) + 0.37)')
plt.plot(x, y_symmetric, label='Symmetric Function')
plt.scatter(3, 0.35, color='red', label='Center Point (3, 0.35)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.title('Symmetric Functions')
plt.show()


