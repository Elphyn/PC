
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a random numpy matrix
A = np.random.rand(50, 50)
# Generate a random solution vector
b = np.random.rand(50)

# solve linalg
x = np.linalg.solve(A, b)
print(f'Result: {x}')

# Heatmap matrix A
plt.figure()
sns.heatmap(A, cmap='coolwarm')
plt.title('Heatmap of Matrix A')
plt.savefig('heatmap_matrix_A.png')
plt.show()
