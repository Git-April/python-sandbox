import numpy
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

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

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))

print(r2_score(y, mymodel(x)))

speed = mymodel(17)
print(speed)

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(2, 95, 100)

# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))

print(r2_score(y, mymodel(x)))

# plt.show()

df = pandas.read_csv('data3.csv')

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)
print(regr.coef_)

predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)

scale = StandardScaler()

df = pandas.read_csv("data3.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

print(scaledX)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

# plt.scatter(x, y)

train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

# plt.scatter(train_x, train_y)
# plt.plot(myline, mymodel(myline))

# plt.show()

r2 = r2_score(train_y, mymodel(train_x))

print(r2)

r2 = r2_score(test_y, mymodel(test_x))

print(r2)

print(mymodel(5))