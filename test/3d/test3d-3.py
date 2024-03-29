
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
n = 1000  # 做1000*1000的点阵

# 用meshgrid生成一个二维数组
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))

z = (1 - x / 2 + x** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
fig = plt.figure()

# ax = plt.gca(projection='3d')  # 返回的对象就是导入的axes3d类型对象

ax = fig.add_subplot(projection = '3d')

plt.title('3D Surface', fontsize=20)

ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)
plt.tick_params(labelsize=10)
ax.plot_surface(x, y, z, rstride=10, cstride=10, cmap='jet')

plt.show()

