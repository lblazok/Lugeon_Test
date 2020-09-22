import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 2 * np.pi, 400)
# y = np.sin(x**2)

# fig, (ax1, ax2) = plt.subplots(1, 2)
# fig.suptitle('Horizontally stacked subplots')
# ax1.plot(x, y)
# ax2.plot(x, -y)

# plt.show()
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.barh([1,2,3,4], [4,3,2,1], align='center')
ax2.barh([1,2,3,4], [4,3,2,1], align='center')
plt.show()