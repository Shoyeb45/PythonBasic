a = input("enter your age:")
b = input("Please enter your name:")
print("Your name is "+b)

#we can use multiple arguments like this

print("the numbers is ",a)

#like this also

print(f"Your name is {b} and your age is {a}")

#also like this

print("Your name is {} and you are {} years old".format(b,a))

#also like this 

print("Your name is", b, "& your age is" , a)

#using separators

d = 1
m = 11
y = 2023
print("Date:")
print(d,m,y ,sep="-" )
