import pandas as pd

# Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game

print("\nWelcome to the KBC quiz")
print("Here is the prize pool")

prizePool = [1000, 10000, 50000, 100000, 200000]
pp = pd.Series(["₹1,000", "₹10,000", "₹50,000", "₹1,00,000", "₹2,00,000"])
pp.index = [1, 2, 3, 4, 5]
print(pp)
print("Note: Every wrong answer will be given -₹1,000")

Questions = ["Q-1. Who created python programming language?", "Q-2. Who is father of computer?", "Q-3. Which is most used programming language in the world?", "Q-4. Which is most energy efficient programming language in world?", "Q-5. Who created the internet?"]

Options = [["Linus Trovald", "Guido van Rossum", "James Gosling", "Dennis Ritchie"] , ["Alan Turing", "Charles Bababage", "Ada Lovelace", "Howard H. Aiken"], ["Python", "Java", "C++", "Javascript"], ["C/C++", "Python", "Java", "Ruby on rails"], ["Robert Cailliau", "Sir Berners-Lee", "Bob Kahn", "Steve Wozniak"]]

answer = ["B", "B", "D", "A", "B"]
print("\n\t\tQuiz!!")



totalPrize = 0
i = 0
while(i <= 4):
    print(f"\n{Questions[i]}\nOptions:")
    print(f"A.{Options[i][0]}\t\tB.{Options[i][1]}\nC.{Options[i][2]}\t\tD.{Options[i][3]}")
    ans = input("Enter correct answer (option only, like A, B, C, D):")
    if ans == answer[i]:
        totalPrize = totalPrize + prizePool[i]
        print(f"Congratulations!! You have enterd correct answer,\nTotal amount till now :₹{totalPrize}")
    else:
        totalPrize = totalPrize - 1000    
        print(f"Ohh!! You have enterd wrong answer,\nTotal amount till now :₹{totalPrize}\nCorrect answer is: {answer[i]}")
    i=i+1

print("Thank you for participating in KBC")

if totalPrize > 0:
    print(f"You have won ₹{totalPrize}/- only.")
else:
    print(f"You have wasted our time pleases give ₹{-totalPrize}/- to our organization.")
