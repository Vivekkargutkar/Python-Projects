'''
user choice - rock, paper, scissor
computer choice - randomly choose in define list
print result

conditions:
a - rock
rock - rock = tie
rock - paper = paper win
rock - scissor = rock win

b - paper
paper - paper = tie
paper - rock = paper win
paper - scissor = scissor win

c - scissor
scissor - scissor = tie
scissor - rock = rock win
scissor - paper = scissor win

'''


import random

items = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your choice: Rock, Paper, Scissor = ")
comp_choice = random.choice(items)

print(f"User Choice= {user_choice}, \nComputer Choice= {comp_choice}")

if user_choice.capitalize() == comp_choice :
    print("Both Chooses Same : Match Tie")

elif user_choice.capitalize() == "Rock":
    if comp_choice == "Paper":
        print("Paper Covers Rock : Computer Wins")
    else :
        print("Rock Smashes Scissor : User Wins")


elif user_choice.capitalize() == "Paper":
    if comp_choice == "Scissor":
        print("Scissor Cuts Paper : Computer Wins")
    else :
        print("Paper Covers Rock : User Wins")


elif user_choice.capitalize() == "Scissor":
    if comp_choice == "Paper":
        print("Scissor Cuts Paper : User Wins")
    else :
        print("Rock Smashes Scissor : Computer Wins")

else:
    print(f"Invalid user choice..{user_choice}\nChoose correct option in given options")
    