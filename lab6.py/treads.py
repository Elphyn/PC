import numpy as np
import time
import multiprocessing as mp
from multiprocessing.shared_memory import SharedMemory
import matplotlib.pyplot as plt

# Set the size of vectors
vector_size = 1000

# Create two random vectors
vec1 = np.random.rand(vector_size)
vec2 = np.random.rand(vector_size)

# Create shared memory for the vectors
vec1_shared = SharedMemory(create=True, size=vec1.nbytes)
vec2_shared = SharedMemory(create=True, size=vec2.nbytes)

# Copy the vectors to the shared memory
np.ndarray(vec1.shape, dtype=vec1.dtype, buffer=vec1_shared.buf)[:] = vec1
np.ndarray(vec2.shape, dtype=vec2.dtype, buffer=vec2_shared.buf)[:] = vec2


def parallel_dot_product(start, end, shared_mem1, shared_mem2, output, lock):
    # Reconstruct the numpy arrays from the shared memory
    vec1 = np.ndarray((end-start,), dtype=np.float64, buffer=shared_mem1.buf)
    vec2 = np.ndarray((end-start,), dtype=np.float64, buffer=shared_mem2.buf)
    
    # Calculate the partial dot product
    partial_result = np.dot(vec1, vec2)
    
    # Lock and update the shared output variable
    with lock:
        output.value += partial_result


def run_parallel_algorithm(num_threads):
    # Calculate the size of the subtasks
    subtask_size = vector_size // num_threads

    # Create a shared output variable for the dot product
    output = mp.Value("d", 0.0)

    # Create a lock for updating the shared output variable
    lock = mp.Lock()

    # Start measuring time
    start_time = time.time()

    # Create the threads (processes) and start them
    threads = []
    for i in range(num_threads):
        start = i * subtask_size
        end = (i+1) * subtask_size if i+1 != num_threads else vector_size
        thread = mp.Process(target=parallel_dot_product, args=(start, end, vec1_shared, vec2_shared, output, lock))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Stop measuring time
    end_time = time.time()

    # Calculate the execution time
    execution_time = end_time - start_time

    return execution_time



def main():
            
    thread_counts = range(1, mp.cpu_count() + 1)
    execution_times = [run_parallel_algorithm(num_threads) for num_threads in thread_counts]


    plt.plot(thread_counts, execution_times, marker='o')
    plt.xlabel("Number of Threads")
    plt.ylabel("Execution Time (s)")
    plt.title("Execution Time vs Number of Threads")
    plt.grid()
    plt.show()

    optimal_threads = thread_counts[np.argmin(execution_times)]
    print(f"Optimal number of threads: {optimal_threads}")


if __name__ == "__main__":
    mp.freeze_support()
    main()


