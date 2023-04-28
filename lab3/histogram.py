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

# Plot a histogram of the solution
plt.figure()
sns.histplot(x, kde=False)
plt.title('Histogram of Solution')
plt.xlabel('Value')
plt.ylabel('Frequency')
# plt.savefig('histogram_solution.png')
plt.show()

