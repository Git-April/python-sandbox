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