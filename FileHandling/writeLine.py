with open("p.txt", "w") as t:
    l = ["sudo apt", "ls -a", "pwd", "grep", "find"]
    t.writelines(l)
    t = open("p.txt", "r")
    fileContent = t.read()
    print(fileContent)