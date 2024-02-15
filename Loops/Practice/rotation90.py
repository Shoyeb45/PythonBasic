# rotating matrix by 90 degree clockwise
# n = 4
# matrix = [[1, 4, 8, 34], 
#           [2, 5, 3, 78], 
#           [3, 6, 2, 54],
#           [3, 8, 1, 19]]

# ans = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# ans[0][1] = 1
# for i in range(0, 4):
#     for j in range(0, 4):
#         ans[j][n-i-1] = matrix[i][j]

# i, j =0, 0
# for i in range(4):
#     for j in range(4):
#         print(ans[i][j],end=" ")
#     print()

m = [[1, 2, 3, 4], 
          [5, 6, 7, 8], 
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
n = 4 
circles = 0
i, j = 0, 0
while (circles < n/2):
    cycles = n - 1 - (2 * circles)
    jump = 0
    while( jump < cycles):
        temp = m[i][j + jump]
        m[i][j+jump] = m[i+cycles-jump][j]
        m[i+cycles-jump][j] = m[i+cycles][j+cycles-jump]
        m[i+cycles][j+cycles-jump] = m[i+jump][j+cycles]
        m[i+jump][j+cycles] = temp
        jump += 1
    i += 1
    j += 1
    circles += 1


for i in range(4):
    for j in range(4):
        print(m[i][j],end=" ")
    print()

