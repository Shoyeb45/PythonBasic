def avg(a=9, b=10):
    print(f"Average of {a} and {b}",(a+b)/2)

avg()  # will take 9 and 10
avg(1, 4) # 1 and 4 will overwrite 9 and 10 
avg(3)  # here a will be 3 and b will be default i.e. 10

def subt(a, b):
    print(f"subtraction of {a} and {b}",a-b)

subt(a=10, b=1)
subt(b=17, a=14)
subt(b=10, a=35)
    
def name(firstName, middleName, lastName):
    print("Hello,", firstName, middleName, lastName)

name("Shoyeb", "Abdul Sattar", "Ansari")

# function only returns the passed argument if value is positive else return value will be 0

def positive(a):
    if(a > 0):
        return a
    else:
        return 0
    
print(f"{positive(9)}")
print(f"{positive(-19)}")

# finding average of n number by function

def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)
    
c = average(12, 12, 24, 34, 12, 9)
print(f"Average of numbers are {c}")