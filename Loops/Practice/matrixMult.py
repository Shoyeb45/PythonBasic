a = [[1, 3, 4], [3, 2, 1], [2, 5, 1]]
b = [[1, 10, -2], [1, -7, 0], [1, 2, -9]]
c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        sum = 0
        for p in range(3):
            sum += a[i][p] * b[p][j]
        c[i][j] = sum

i, j =0, 0
for i in range(3):
    for j in range(3):
        print(c[i][j],end=" ")
    print()