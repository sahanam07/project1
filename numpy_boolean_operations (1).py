import numpy as np

arr = np.array([10, 25, 30, 45, 60, 15, 50])

filtered_arr = arr[(arr > 20) & (arr < 50)]

print(filtered_arr)