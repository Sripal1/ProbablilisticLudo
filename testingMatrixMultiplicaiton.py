import numpy as np
from numpy import linalg

# # Create a 2x2 matrix
# A = numpy.matrix([[1, 2], [3, 4]])

# #multiply the matrix by itself
# B = A * A

# print(B)

# C = numpy.random.randint(0, 10, (58, 58)) #58x58 matrix
# D = numpy.random.randint(0, 10, (58, 1)) #58x1 matrix

# print("\n\n")
# print("\n58x58 matrix:")
# print(C) #58x58 matrix
# print("\n\n")
# print("\n58x1 matrix:")
# print(D) #58x1 matrix
# print("\n\n")

# product = (C * D)
# print("Shape of C:", C.shape)
# print("Shape of D:", D.shape)
# print("Shape of product:", product.shape)

# reshaped_product = product.reshape((3364))
# reshaped_product = reshaped_product.reshape((3364,1))
# print("Shape of reshaped product:", reshaped_product.shape)
# print(reshaped_product)
# print("\n\n")

# product = numpy.dot(C, D) #58x58 * 58x1 = 58x1 using linalg module from numpy
# print("Product of 58x58 and 58x1 matrix:")
# print(product)
# print("\n\n")

matrix = np.zeros((76,76))
np.set_printoptions(threshold=np.inf)  # set print options to display all elements of matrix
print(matrix)
