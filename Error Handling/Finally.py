try:
    a = int(input("Enter a real part of complex number:"))
    b = int(input("Enter a imaginary part of complex number:"))
    z = complex(a, b)
    print(z)
except ValueError:
    print("Invalid input.")
else:
    print("Correct input.")
finally:
    print("I will always going to be executed.")

# Example with function 
    
def fun():
    try:
        l = [1,2, 4, 3]
        f = int(input("Enter some random number:"))
        print(l[f])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always executed")

x = fun()
print(x)


 