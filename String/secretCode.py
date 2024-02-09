# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language
# Coding - if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end else: simply reverse the string
# decoding - if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode
print("This is program to code and decode code word.")
def code(s):
    if len(s) >= 3:
        a = list(s)
        a1 = a.pop(0)
        a.append(a1)
        a.append('w')
        a.append('e')
        a.append('q')
        a.insert(0, 'r')
        a.insert(0, 'u')
        a.insert(0, 'p')
        return a
    else:
        return s[::-1]

def decode(s):
    if len(s) < 3:
        return s[::-1]
    else:
        a = list(s)
        i = 1
        while(i <= 3):
            a.pop(0)
            a.pop()
            i = i + 1
        a1 = a.pop()
        a.insert(0, a1)
        return a

        

word = input("Enter word:")
choice = input("Do you want to code the given word or decode (write simple code or decode) :")

if choice == 'code':
    ans = ""
    for i in code(word):
        ans += i
    print(f"{word} is coded in : {ans}")
elif choice == 'decode': 
    ans = ""
    for i in decode(word):
        ans += i
    print(f"decoded {word} is : {ans}")



