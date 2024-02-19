a = int(input("Enter the 2 number:\n"))
b = int(input())

# function for finding maximum number between two numbers

def Max(a, b):
    if(a > b):
        print("The maximum number is",a)
    else:
        print("The maximum number is",b)

Max(a, b)   # Function call

def greet(msg):
    print(msg)

f = greet("Hello world")
print(f)    # as it is not returning anything so it will return none value.