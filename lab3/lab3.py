import numpy as np
import matplotlib.pyplot as plt

# Generate a random numpy matrix
A = np.random.rand(50, 50)
# Generate a random solution vector
b = np.random.rand(50)

# solve linalg
x = np.linalg.solve(A, b)
print(f'Result: {x}')

# Heatmap matrix A
plt.imshow(A, cmap='coolwarm')
# coolwarm pallet

# Heatmap right
plt.colorbar()
# solution vector
plt.title('Heatmap of Matrix A')
plt.show()

# Plot a histogram of the solution
plt.hist(x)

# 
plt.title('Histogram of Solution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# seaborn для гистограмы
# гистограмму случ массива отдельно