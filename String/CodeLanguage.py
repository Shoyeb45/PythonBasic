# improved version of secretCode
import string
import random

print("This is program to code and decode code word.")
def code(s):
    if len(s) >= 3:
        a = list(s)
        a1 = a.pop(0)
        a.append(a1)
        i = 1
        while(i<=3):
            randLetter = random.choice(string.ascii_letters)
            a.append(randLetter)
            a.insert(0, random.choice(string.ascii_letters))
            i = i + 1
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

        

word = input("Enter your message:")
choice = input("Do you want to code the given word or decode (Simply write 'code' or 'decode') :")

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

