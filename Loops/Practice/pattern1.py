n = 6

# for i in range(0, 5):
#     for j in range(5):
#         if(j <= i or j<=n-1-i):
#             print("*", end='')
#         else:
#             print(" ",end = ' ' )
#     print()

n = 50
for i in range(0, n):
    for j in range(0, n):
        if(i == j or i+j == n-1):
            print("\\", end=" ")
        else:
            if j == n-1-i:
                print("/", end=" ")
            else:
                print("*",end=' ')
    print()