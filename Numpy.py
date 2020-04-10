import numpy as np
import matplotlib.pyplot as plt

a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)])
print(a)
print("Size of the array: ", a.size)
print("Shape of the array: ", a.shape)
print("Dimension of the array: ", a.ndim)
print("Data Type of the array: ", a.dtype)
print("Memory (bytes) used by one element: ", a.itemsize)
print()

b = a.reshape(2, 6)
print("New reshaped array: ", b)
print()

# Slicing of the array
print("Slicing of the arrey")
print(a[0:, 2])
print(a[0:2, 2])
print(a[1:3, 1:])
print(a[1:3, 0:2])

a = np.array([(1, 2, 3, 4),  (5, 6, 7, 8), (9, 10, 11, 12)])
print(a[1:2, 1:3])
print('Minimun: ', a.min())
print('Maximum: ', a.max())
print('Sum: ', a.sum())
print('Sum of rows: ', a.sum(axis=1))
print('Sum of columns: ', a.sum(axis=0))

print("\nLinespace: ", np.linspace(0, 10, 5))
print()

# Vertical and Horizontal Stacking
print("Vertical and Horizontal Stacking")
a = np.array([(1, 2, 3), (4, 5, 6)])
b = np.array([(1, 2, 3), (4, 5, 6)])
print(np.vstack((a, b)))
print(np.hstack((a, b)))
print()

# To convert 2D array into a single column array
print("To convert 2D array into a single column array")
print(a.ravel())

# Sin, Cos, Tan functions
print("Sin, Cos, Tan functions")
x = np.arange(0, 2*np.pi, 0.1)
y = np.tan(x)
plt.plot(x, y)
plt.show()

