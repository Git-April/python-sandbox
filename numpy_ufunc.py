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