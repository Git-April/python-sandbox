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

plt.hist(x, 5)

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 5)
plt.show()