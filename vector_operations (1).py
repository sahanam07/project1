import numpy as np

celsius = np.random.uniform(15.0, 40.0, 10)

print("Temperature in Celsius:")
print(celsius)

fahrenheit = (celsius * 9 / 5) + 32

print("\nTemperature in Fahrenheit:")
print(fahrenheit)

numbers = np.arange(1, 11)
square_roots = np.sqrt(numbers)

print("\nNumbers:")
print(numbers)

print("\nSquare Roots:")
print(square_roots)

max_index = np.argmax(fahrenheit)

print("\nIndex of maximum Fahrenheit temperature:")
print(max_index)

print("\nMaximum Fahrenheit temperature:")
print(fahrenheit[max_index])