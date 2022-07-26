import numpy as np

a = np.array([2,4,5])
print(a)

b = np.array([[3,7,5],[6,9,7]])
print(b)

#dimension
print(a.ndim)

#shape
print(b.shape)

#datatype
print(a.dtype)

#get size in bytes
print(a.itemsize)

#Total number of elements
print(a.size)

#Total number of size(itemsize * size)
print(b.nbytes)