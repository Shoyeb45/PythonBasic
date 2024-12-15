from concurrent.futures import ProcessPoolExecutor
import time
import numpy as np

def square_number(number):
    time.sleep(1)
    return f"squre of number {number} is : {number ** 2}"

if __name__ == "__main__":
    numbers = np.ndarray()

    init_time = time.time()
    with ProcessPoolExecutor(max_workers = 3) as executer:
        results = executer.map(square_number, numbers)

    for result in results:
        print(result)

    print(time.time() - init_time)