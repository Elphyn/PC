import numpy as np
import torch
import time

# Set the dimensions of the matrices
m = 4000
n = 4000
p = 4000

# Create the matrices as lists
matrix1 = [[i+j for j in range(n)] for i in range(m)]
matrix2 = [[i*j for j in range(p)] for i in range(n)]

# Multiply the matrices and measure the time taken
# start_time = time.time()
# result_list = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
# end_time = time.time()
# print("Time taken to multiply matrices as lists: ", end_time - start_time)

# Convert the matrices to NumPy arrays and perform the multiplication again, measuring the time taken
matrix1_np = np.array(matrix1)
matrix2_np = np.array(matrix2)
start_time = time.time()
result_np = np.matmul(matrix1_np, matrix2_np)
end_time = time.time()
print("Time taken to multiply matrices as NumPy arrays: ", end_time - start_time)

# Convert the matrices to PyTorch tensors and perform the multiplication again, measuring the time taken
matrix1_torch = torch.tensor(matrix1)
matrix2_torch = torch.tensor(matrix2)
start_time = time.time()
result_torch = torch.matmul(matrix1_torch, matrix2_torch)
end_time = time.time()
print("Time taken to multiply matrices as PyTorch tensors: ", end_time - start_time)



# Time taken to multiply matrices as lists:  9.3880774974823
# Time taken to multiply matrices as NumPy arrays:  0.0801534652709961
# Time taken to multiply matrices as PyTorch tensors:  0.2147974967956543


# Time taken to multiply matrices as NumPy arrays:  313.75464153289795
# Time taken to multiply matrices as PyTorch tensors:  414.8475830554962

# 176.124.215.22:60023