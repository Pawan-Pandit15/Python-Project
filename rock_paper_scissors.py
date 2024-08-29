#  Rock Paper Scissors Game
'''
Project Work Flow

user input (rock, paper, scissors)
computer choice ( computer will choice randomly not conditionally )
result print

Cases:
Rock-
rock = rock -----> tie
rock = paper ----> paper win
rock = scissor ---> rock win

Paper-
paper = paper ------> tie
paper = rock -------> paper win
paper = scissor ----> scissor win

Scissor-
scissor = scissor -----> tie
scissor = paper -------> scissor win
scissor = rock --------> rock win
'''

import random
items_list = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter Your Choice (Rock, Paper, Scissor) : ")
comp_choice = random.choice(items_list)
print(f"user choice = {user_choice},computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both Chooses Same: = Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper cover Rock = Computer Win")
    else:
        print("Rock Smashes Scissor = You Win")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper cover Rock = You Win")
    else:
        print("Scissor Cut Paper = Computer Win")
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor Cut Paper = You Win")
    else:
        print("Paper cover Rock = Computer Win")

else:
    print("Invalid Input")
