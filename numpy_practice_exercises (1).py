import numpy as np

matrix = np.random.randint(1, 51, (5, 5))

print("Original Matrix:")
print(matrix)

greater_25 = matrix[matrix > 25]

print("\nNumbers greater than 25:")
print(greater_25)


matrix_even_zero = matrix.copy()
matrix_even_zero[matrix_even_zero % 2 == 0] = 0

print("\nMatrix after replacing even numbers with 0:")
print(matrix_even_zero)


x = np.random.randint(1, 51, 10)

normalized = (x - np.min(x)) / (np.max(x) - np.min(x))

print("\nOriginal 1D Array:")
print(x)

print("\nNormalized Array:")
print(normalized)