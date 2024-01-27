a = int(input("Enter the number:"))

for i in range(13):
    if(i == 10):
        break
    print(a,"*",i+1,"=",a*(i+1))

print()

for i in range(13):
    if(i == 10):
        print("Skip the iteration")
        continue
    print(a,"*",i,"=",a*(i))


