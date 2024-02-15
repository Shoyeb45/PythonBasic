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

n = 4 
circles = 0
i, j = 0, 0
matrix = [[1, 4, 8, 34], 
          [2, 5, 3, 78], 
          [3, 6, 2, 54],
          [3, 8, 1, 19]]
count = 0
while (circles < n//2):
    cycles = n - 1 - 2 * circles
    jump = 0
    while( jump < cycles):
        temp = matrix[i][j + jump]
        matrix[i][j+jump] = matrix[i+cycles-jump][j]
        matrix[i+cycles][j+cycles-jump] = matrix[i+jump][j+cycles]
        matrix[i+jump][j+cycles] = temp
        jump += 1
    i += 1
    j += 1
    circles += 1

i, j =0, 0
for i in range(4):
    for j in range(4):
        print(matrix[i][j],end=" ")
    print()

