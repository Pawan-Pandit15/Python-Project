#
# Task #1 - Take a user input (name, age, roll_number, phone_number)
# # and print the user details.


# u1=input("Enter User Name :")
# u2=input("Enter User Age :")
# u3=input("Enter User Roll_Number :")
# u4=input("Enter User Phone_Number :")
# print('',u1,'\n',u2,'\n',u3,'\n',u4,)


# Task #2 - Print the Table of 2 by using the command print()
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 10 = 20

# Option 1 using command print

# print(f"2 x 1 = {2*1}")
# print(f"2 x 2 = {2*2}")
# print(f"2 x 3 = {2*3}")
# print(f"2 x 4 = {2*4}")
# print(f"2 x 5 = {2*5}")
# print(f"2 x 6 = {2*6}")
# print(f"2 x 7 = {2*7}")
# print(f"2 x 8 = {2*8}")
# print(f"2 x 9 = {2*9}")
# print(f"2 x 10 = {2*10}")


# Option 2 using for loop

num=int(input("enter the number:"))
for i in range(1,11):
    print(num,"X",i,"=",num*i)
