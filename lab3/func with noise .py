import matplotlib.pyplot as plt
import numpy as np
__author__ = "Vlad Karelov"

# Define the complex function
def complex_function(x):
    return np.sin(x) + 0.5 * np.cos(2 * x)

# Generate the data
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = complex_function(x)

# Add noise to the data
noise = np.random.normal(0, 0.2, y.shape)
y_noisy = y + noise

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Original function', color='blue')
plt.plot(x, y_noisy, label='Function with noise', color='red', linestyle='dashed')

# Add labels, title, legend, and grid
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Graph of Complex Function')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()

