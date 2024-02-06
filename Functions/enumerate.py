colors = ["Blue", "Green", "Black", "Yellow", "Pink", "White"]

for index, value in enumerate(colors):
    print(index, value)

l = ("Java", "Kotlin", "C Language", "C++", "Python", "GoLang")

print("\tTuple example\n")
for i, val in enumerate(l):
    print(i, val)

# changing index of list
print("\tColors")
for index, value in enumerate(colors, start=1):
    print(index, value)

str = "Vivaan Cheeda"

for ind, value in enumerate(str):
    print(f"letter number {ind+1} is {value}")

