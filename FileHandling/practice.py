file = open("p.txt")
print(f"{file.read()}")

file = open("p.txt", 'w')
file.write("This will overwrite the content of original file")
print(f"{file.readable()}")
file.close()

