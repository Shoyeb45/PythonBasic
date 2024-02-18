# finding row where maximum number of 1 is present

m, n = 5, 5
a = [[0, 0, 0, 0, 1], [0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 1, 1]]

row, minIndex = -1, 2147483647

for i in range(m):
    lower, upper = 0, n - 1
    ind = minIndex  
    while lower <= upper:
        mid = (lower + upper) // 2
        if mid != 0 and a[i][mid] == 1 and a[i][mid - 1] == 0:
            ind = mid
            break  
        elif mid == 0 and a[i][mid] == 1:
            ind = 0
            break  
        elif a[i][mid] == 1:
            upper = mid - 1
        elif a[i][mid] == 0:
            lower = mid + 1

    if ind < minIndex:
        minIndex = ind
        row = i + 1

print(row)
