# opening a file

file = open('requirement.txt', 'r' )
# print(file)

# accessing file content
text = file.read()
print(text)
file.close()

w = open('requirement.txt', 'w')

w.write("This file contains very important information, so please don't try to peek in file.")
w.close()

# creating new file

# newFile = open("Hello.txt", "x")
newFile = open("Hello.txt", "a")

# appending to a file
newFile.write("Hello, how are you? ")
newFile.close()


with  open("Info.txt", 'w') as t:
    t.write("Python is very useful programming language.")