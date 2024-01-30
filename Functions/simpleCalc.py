def add(a, b):
    return a+b
def mult(a, b):
    return a*b
def div(a, b):
    return a/b
def subt(a, b):
    return a-b

a = float(input("Enter number a:"))
b = float(input("Enter number b:"))

c = input("Choose operator:")
match c:
    case '+':
        print(a,"+",b,"=",add(a,b))
    case '-':
        print(a,"-",b,"=",subt(a,b))
    case '/':
        print(a,"/",b,"=",div(a,b))
    case '*':
        print(a,"*",b,"=",mult(a,b))
    case _:
        print("Enter valid operation")

