x = 7

def f():
    x = 91
    print("The local value of x is",x)

print("The global value of x is",x)

f()
y = 12
def g():
    global x 
    global y 
    x = 10
    y = 73

print(f"x = {x}, y = {y}")
