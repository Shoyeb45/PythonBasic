a = [[0, 0, 0, 0, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 1, 1]]

def MaxRow(a, n, m):
    j = m - 1
    ind, minInd, row = n, 234243244, -1
    for i in range(n):

        while (j >= 0):
            if a[i][j] == 0:
                # j = j - 1
                ind = j + 1
                break
            ind = j
            j -= 1

        if ind < minInd:
            minInd = ind
            row = i + 1
    
    return row
    
print(MaxRow(a, 5, 5))