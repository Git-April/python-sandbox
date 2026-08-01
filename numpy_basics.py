#NumPy HOME
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

#NumPy Getting Started
arr = np.array([1, 2, 3, 4, 5])

print(arr)

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(np.__version__)

#NumPy Creating Arrays
array = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

array = np.array((1, 2, 3, 4, 5))

print(arr)

arr = np.array(42)
print(arr)

arr = np.array([1, 2, 3, 4, 5])

print(arr)

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim) #new
print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5) #new
print(arr)
print('number of dimensions :', arr.ndim)

#NumPy Array Indexing
arr = np.array([1, 2, 3, 4])

print(arr[0])

arr = np.array([1, 2, 3, 4])

print(arr[1])

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('2nd element on 1st row: ', arr[0,1])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('5th element on 2nd row: ', arr[1, 4])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Last element from 2nd dim: ', arr[1, -1])

#NumPy Array Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])

#NumPy Data Types
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype="i4")
print(arr)
print(arr.dtype)

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

#NumPy Copy vs View
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

#NumPy Array Shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) #new

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array: ', arr.shape)

#MumPy Array Reshape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3) #new
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

#NumPy Array Iterating
arr = np.array([1, 2, 3])

for x in arr:
  print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

#NumPy Array Join
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))
print(arr)