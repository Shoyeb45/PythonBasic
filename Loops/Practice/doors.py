import math as mt

n = int(input())

a = []

for i in range(1, n+1):
    a.insert(i, 0)

for i in range(1, n+1):
    x = mt.sqrt(i)
    if(int(x) * int(x) == i):
        print(f"{i} door is closed.")
    else:
        print(f"{i} door is opened.")