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