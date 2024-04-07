with open("metaData.txt", "r") as f:
    l = f.readlines()
    for str in l:
        print(str)

print()
with open("metaData.txt", "r") as f:
    l = f.readline()
    while l:
        print(l, end = " ")
        l = f.readline()

