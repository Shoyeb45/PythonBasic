str = "My name is Shoyeb Ansari"

# i is iterator, it is starting from 0
for i in str:
    print(i,end="-")

print()    

colors = ["blue", "red", "Green", "violet", "Purple"]

for color in colors: # color is the variable which is iterating over list colors
    print(color)
    # we can also iterate over color, since it is string
    for char in color:
        print(char)

# printing number from 1 to 100
        
for k in range(1, 101):
    print(k,end=" ")

print()
# printing odd number between 1 to 50
    
for i in range(1, 51, 2):
    print(i, end=" ")


print()
colors = ["blue", "red", "Green", "violet", "Purple"]

for i in range(0, len(colors)):
    print(colors[i])

# iterating over dictionary
d1 = {
    "Name" : "Navneet Sharma",
    "Age": 19,
    "Profession" : "Student"
}

for key,value in d1.items():
    print(key,":", value)


# for-else loop
print("\n")
    
o = (12, 56, -98, 10, 12, -75, -12)

for i in o:
    print(i)
else:
    print("Came out of loop")