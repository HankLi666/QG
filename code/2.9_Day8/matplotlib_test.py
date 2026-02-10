# 配合 Matplotlib 画图，用 NumPy 生成 x 轴数据，绘制正弦曲线

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4)) # 设置画布大小
plt.plot(x, y, label='Sine Wave', color='#1B3008', linewidth=2) # 曲线图

# 设置x，y坐标的标签
plt.xlabel("x")
plt.ylabel("sin(x)")

# 图表装饰
plt.title('sinesoid')
plt.legend()

plt.show()