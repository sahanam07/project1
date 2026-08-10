import numpy as np

arr = np.arange(1, 21)

print("1D Array:")
print(arr)

matrix = arr.reshape(4, 5)

print("\n4 × 5 Matrix:")
print(matrix)

columns = matrix[:, 1:3]

print("\n2nd and 3rd Columns:")
print(columns)

corners = np.array([
    matrix[0, 0],   # Top-left
    matrix[0, -1],  # Top-right
    matrix[-1, 0],  # Bottom-left
    matrix[-1, -1]  # Bottom-right
])

print("\nFour Corner Elements:")
print(corners)