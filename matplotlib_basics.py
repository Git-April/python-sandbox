import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

xpoints = np.array([0, 6])
ypoints = np.array([0, 2])
plt.plot(xpoints, ypoints)

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints)

xpoints = np.array([2, 9])
ypoints = np.array([4, 11])
plt.plot(xpoints, ypoints, 'o')

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, ypoints)

ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)

plt.plot(ypoints + 1, marker = 'o')
plt.plot(ypoints)

plt.plot(ypoints + 2, marker = '*')
plt.plot(ypoints)

plt.plot(ypoints + 3, 'o:r')
plt.plot(ypoints)

plt.plot(ypoints + 4, marker = 'o', ms = 10)
plt.plot(ypoints)

plt.plot(ypoints + 5, marker = 'o', ms = 10, mec = 'r')
plt.plot(ypoints)

plt.plot(ypoints + 6, marker = 'o', ms = 10, mfc = 'g')
plt.plot(ypoints)

plt.plot(ypoints + 7, marker = 'o', ms = 10, mfc = 'g', mec = 'b')
plt.plot(ypoints)

plt.plot(ypoints + 8, marker = 'o', ms = 10, mfc = '#FF00FF', mec = '#00FF00')
plt.plot(ypoints)

plt.plot(ypoints + 9, marker = 'o', ms = 10, mfc = 'pink', mec = 'green')
plt.plot(ypoints)

plt.plot(ypoints + 10, linestyle = 'dotted')
plt.plot(ypoints)

plt.plot(ypoints + 11, linestyle = 'dashed')
plt.plot(ypoints)

plt.plot(ypoints + 12, ls = ':')
plt.plot(ypoints)

plt.plot(ypoints + 13, color = 'r')
plt.plot(ypoints)

plt.plot(ypoints + 14, c = '#FF00CC')
plt.plot(ypoints)

plt.plot(ypoints + 14, c = 'lightgreen')
plt.plot(ypoints)

plt.plot(ypoints + 15, linewidth = '3.5')
plt.plot(ypoints)

x1 = np.array([0, -1])
y1 = np.array([0, -1])
x2 = np.array([3, -1])
y2 = np.array([3, -1])
plt.plot(x1, y1, x2, y2)

plt.show()