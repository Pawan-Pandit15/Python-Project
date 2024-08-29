print("----------Welcome To BIG & SMALL Game------------")

import random

items = ["Big", "Small"]

user_input = input("Choose ( Big or Small ) : ")
user_input_amount = int(input("Enter Amount : "))
comp_choice = random.choice(items)
Total_Amount = 100
win_amount = 0

if user_input == comp_choice:
    print("You Win")
    win_amount += user_input_amount * 2
    win_amount -= win_amount * 0.04
    win_amount = win_amount - user_input_amount
    tax = user_input_amount - win_amount
    print("Tax 4% :", tax)

else:
    print("You Lose")


balance = user_input_amount + win_amount

print("Win Amount", win_amount)
print("User Enter : ", user_input)
print("Computer Enter : ", comp_choice)
print("Your Total Amount :", balance)
