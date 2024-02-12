mat = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

for i in range(5):
    for j in range(5):
        mat[i][j] = 0


rowCnt, colCnt = 5, 5
k =  1
i, j= 0, 0
while ( rowCnt > 0 and colCnt > 0):
    jump = 0
    # L to R
    while (jump < colCnt):
        mat[i][j] = k
        k += 1
        j += 1
        jump += 1
    colCnt -= 1

    # T to B
    i += 1
    j -= 1
    while (jump < rowCnt):
        k += 1
        i += 1
        jump += 1


for i in range(5):
    for j in range(5):
        print(mat[i][j], end=" ")
    print()