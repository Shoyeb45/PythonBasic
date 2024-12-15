from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number is : {number}"


numbers = [1,2,3,4,5,6]
init_time = time.time()
with ThreadPoolExecutor(max_workers = 3) as executer:
    results = executer.map(print_number, numbers)

for result in results:
    print(result)
print(time.time() - init_time)