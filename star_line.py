from numpy.random import rand, randint
from matplotlib.collections import LineCollection

import numpy as np
import matplotlib.pyplot as plt

N, L = 20, 100  # 流星个数和线段数
ts = np.array([
    np.linspace(0, rand(), L) for _ in range(N)]).T
x0, y0 = rand(2 * N).reshape(2, 1, N)
x0 *= 5
xs, ys = x0 + ts, y0 + ts  # 绘图线条1

points = np.array([xs, ys]).T.reshape(N, L, -1, 2)

ax = plt.subplot()
for i in range(N):
    segs = np.concatenate([points[i][:-1], points[i][1:]], axis=1)
    lc = LineCollection(segs, cmap='viridis')
    lc.set_array(ts[:, i])
    lc.set_linewidth(ts[::-1, i])
    ax.add_collection(lc)

ax.set_xlim(0, 6)
ax.set_ylim(-2, 3)
ax.set_axis_off()  # 取消坐标轴
plt.show()