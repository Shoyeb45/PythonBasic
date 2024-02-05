a = int(input("Enter number a:"))
b = int(input("Enter number b:"))

print(f"{a} is greater than {b}") if a > b else print(f"{a} is less than {b}")

# multiple conditions 

print("A") if a > b else print("=") if a == b else print("B")


c = 9 if a>b else 0
print(c)