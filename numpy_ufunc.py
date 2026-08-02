import numpy as np #ufunc Intro
from math import log #ufunc Logs

#ufunc Intro
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z)

#ufunc Create Function
def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

print(type(np.add))

print(type(np.concatenate))

if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')

#ufunc Simple Arithmetic
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)
print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)
print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.multiply(arr1, arr2)
print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
newarr = np.divide(arr1, arr2)
print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])
newarr = np.power(arr1, arr2)
print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.mod(arr1, arr2)
print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.remainder(arr1, arr2)
print(newarr)


arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.divmod(arr1, arr2)
print(newarr)

arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)

#ufunc Rounding Decimals
arr = np.trunc([-3.1666, 3.6667])
print(arr)

arr = np.around(3.1666, 2)
print(arr)

arr = np.floor([-3.1666, 3.6667])
print(arr)

arr = np.ceil([-3.1666, 3.6667])
print(arr)

#ufunc Logs
arr = np.arange(1, 10)
print(np.log2(arr))

arr = np.arange(1, 10)
print(np.log10(arr))

arr = np.arange(1, 10)
print(np.log(arr))

nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))

#ufunc Summations
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.add(arr1, arr2)
print(newarr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(newarr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)

arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr)

#ufunc Products
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2], axis=1)
print(newarr)

arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)

#ufunc Differences
arr = np.array([12, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)

arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)
print(newarr)

#ufunc Finding LCM
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)

arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x)

#ufunc Finding GCD
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)

#ufunc Trigonometric
x = np.sin(np.pi/2)
print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)

arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)

x = np.arcsin(1.0)
print(x)

arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)

base = 3
perp = 4
x = np.hypot(base, perp)
print(x)

#ufunc Hyperbolic
x = np.sinh(np.pi/2)
print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print(x)

x = np.arcsinh(1.0)
print(x)

arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)