import numpy
from scipy import stats
import matplotlib.pyplot as plt

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)
print(x)

x = numpy.median(speed)
print(x)

x = stats.mode(speed)
print(x)

x = numpy.std(speed)
print(x)

x = numpy.var(speed)
print(x)

x = numpy.percentile(speed, 0.75)
print(x)

x = numpy.random.uniform(0.0, 5.0, 250)
print(x)

# plt.hist(x, 5)

x = numpy.random.uniform(0.0, 5.0, 100000)

# plt.hist(x, 5)

x = numpy.random.normal(5.0, 1.0, 100000)

# plt.hist(x, 100)

# plt.scatter(speed, speed)

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

# plt.scatter(x, y)

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

# plt.scatter(x, y)
# plt.plot(x, mymodel)

print(r)
speed = myfunc(10)
print(speed)

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)
mymodel = list(map(myfunc, x))

# plt.scatter(x, y)
# plt.plot(x, mymodel)

print(r)

plt.show()