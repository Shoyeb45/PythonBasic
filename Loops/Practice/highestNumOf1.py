a = [[0, 0, 0, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
li = [0, 0, 0, 0, 0]

n, m = 5, 5
for i in range(n):
    for j in range(m):
        li[i] += a[i][j]

max = 0
for i in range(n):
    if (max < li[i]):
        max = li[i]

for i in range(n):
    if (max == li[i]):
        print(i+1)
        break