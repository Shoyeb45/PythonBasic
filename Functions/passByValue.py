def modify(a):
    a += 1
    print("Inside function",a)

a = 19

print("Outside the function without calling",a)
modify(a)
print("Outside the function after calling",a)

list = [1, 3 , 4]

print(list)
def modifyList(list):
    list.appen(9)
    print(list)

modifyList(list)
print(list)