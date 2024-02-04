a = input("Enter a number:")

# printing a table - if user inputs some string value then we'll get some error so we'll cosider these blocks of codes in try.

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:   # this will print what error has occured
#     print(e)

# or we can print some msg in place of error

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:   # this will print what error has occured
    print("Please enter number, not string.")

# if error has occured, then still program will run.
    
print("Did interpreter reached here.")
print("I think yes")

# going to except block of code with specific error type:

try:
    b = int(input("Enter a number:"))
    l = [12, 54, 34, 98, 234]
    print(l[b])
except ValueError:
    print("Please enter a number")
except IndexError:
    print("Please enter number till 4.")