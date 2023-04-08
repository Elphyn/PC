import matplotlib.pyplot as plt
import numpy as np
__author__ = "Vlad Karelov"


x = np.arange(-10, 11, 0.1)

# Calculate the y values for each x using the sin function
y = np.sin(x)/np.abs(x)

# Add some random noise to y
y_noise = y + np.random.normal(0, 0.2, len(y))


plt.plot(x, y, label='sin(x)')
# alpha is transparensy
plt.plot(x, y_noise, 'bo', alpha=0.5, label='$\\frac{sin(x)}{abs(x)}$')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of sin(x)/abs(x) with Noise')
plt.legend()

# Show the plot
plt.show()


# sin заменить на что то посложней
