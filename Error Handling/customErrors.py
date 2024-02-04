

a = int(input("Enter number between 10 and 20:"))

if(a < 10 or a > 20):
    raise ValueError("Please enter number between 10 to 20.")
else:
    print("Good")

class NewError(Exception):
        '''Invalid input...!'''
        pass

try:
    a = input("Enter a number between 10 and 20:")
    if a == 'quit':
         print("Nothing wrong")
         pass
    if int(a) < 10 or int(a) > 20:
         raise NewError()
    else:
        print("Good work.")
except NewError as e:
     print(e)
