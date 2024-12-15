## Processes that run in parallel
### CPU-Bound Tasks-Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
## Parallel execution- Multiple cores of the CPU

import multiprocessing
import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"Square of {i} is {i ** 2}")
    
def cube_number():
    for i in range(5):
        time.sleep(1)
        print(f"Cube of {i} is {i ** 3}")


if __name__ == "__main__":
    # Create process
    process_1 = multiprocessing.Process(target = square_number)
    process_2 = multiprocessing.Process(target = cube_number)
    # initial time
    start_time = time.time()

    # Start the process
    process_1.start()
    process_2.start()

    # Join both processes
    process_1.join()
    process_2.join()

    end_time = time.time()

    print("Time taken:", end_time - start_time) 