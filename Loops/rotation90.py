# rotating matrix by 90 degree clockwise
n = 3
matrix = [[1, 4, 8], 
          [2, 5, 3], 
          [3, 6, 2]]

ans = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
ans[0][1] = 1
for i in range(0, 3):
    for j in range(0, 3):
        ans[j][n-i-1] = matrix[i][j]

i, j =0, 0
for i in range(3):
    for j in range(3):
        print(ans[i][j],end=" ")
    print()