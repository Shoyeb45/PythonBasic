n = int(input())

a = []

for i in range(1, n+1):
    a.insert(i, 0)

for i in range(1, n+1):
    for j in range(1, n+1, i):
        if a[j] == 1:
            a.insert(j, 0)
        else:
            a.insert(j, 1)


for i in range(1, n+1):
    if a[i] == 1:
        print(f"Door {i} is open")
    else:
        print(f"Door {i} is close")