# function to calculate fatorial of a number

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n*factorial(n-1)

# calling function

a = int(input("Enter number:"))
print(factorial(a))

# let's calculate fibonacci series upto n-terms

def fibonacci(n, a):
    if( a == 0 or a == 1):
        print(a," ")
        a=a+1
    else:
        

