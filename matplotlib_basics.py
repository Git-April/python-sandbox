import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

plt.subplot(2, 3, 1)

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
y1 = np.array([1, -1])
x2 = np.array([2, -1])
y2 = np.array([3, -1])
plt.plot(x1, y1, x2, y2)

font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}

plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)
plt.title("Sports Watch Data", fontdict=font1, loc = 'left')

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5, axis = 'x')
plt.grid(axis = 'y')

plt.subplot(2, 3, 2)
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
colors = np.array(['green', 'red', 'blue', 'pink'])
colors2 = np.array([0, 25, 50, 100])
sizes = np.array([252, 360, 324, 445])
plt.scatter(xpoints, ypoints, c=colors, s=sizes, alpha=0.5)
plt.scatter(ypoints, xpoints, c = colors2, cmap='viridis')
plt.colorbar()
plt.title("Sports Watch Data", fontdict=font2, loc = 'left')

plt.suptitle("MY SHOP")

plt.subplot(2, 3, 3)
x = np.array(["A", "B", "C", "D"])
z = x
y = np.array([3, 8, 1, 10])

plt.barh(x, y, color='blue', height = 0.1)

plt.subplot(2, 3, 4)
x = np.random.normal(170, 10, 250)
plt.hist(x)

plt.subplot(2, 3, 5)
y = np.array([252, 360, 324, 445])
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = z, startangle=90, explode=myexplode, shadow=True, colors=colors)
plt.legend(title="Four Fruits")

plt.show()