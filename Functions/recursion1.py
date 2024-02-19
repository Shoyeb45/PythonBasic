l = [1, 2, 3, 4, 6]

def p(a, i):
    if(i == len(a) - 1):
        print(a[i])
        return

    print(a[i])
    p(a, i+1)

p(l, 0)


