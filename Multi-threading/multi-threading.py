import threading 
import time

### Multithreading
## When to use Multi Threading
###I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.


def print_number():
    for i in range(5):
        time.sleep(1)
        print("Number:",i)

def print_letters():
    for i in "abcde":
        time.sleep(1)
        print("Character:", i)


# Creating thread
thread_1 = threading.Thread(target = print_letters)
thread_2 = threading.Thread(target = print_number)

init_time = time.time()

# start threads
thread_1.start() # will execute print_letter()
thread_2.start() # will execute print_number()


# Join both thread to single thread
thread_2.join()
thread_1.join()
end_time = time.time()

print("Total Time", end_time - init_time)