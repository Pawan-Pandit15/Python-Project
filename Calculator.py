
# ********  Calculator Using Print Function ********

num1=10
num2=20
print("Addition of :",num1,"+",num2,"=",num1+num2)
print("Subtraction of :",num1,"-",num2,"=",num1-num2)
print("Multiplication of :",num1,"*",num2,"=",num1*num2)
print("Division of :",num1,"/",num2,"=",num1/num2)




# ********  Calculator Using User Input  ********


num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number :"))

print("Addition of :",num1,"+",num2,"=",num1+num2)
print("Subtraction of :",num1,"-",num2,"=",num1-num2)
print("Multiplication of :",num1,"*",num2,"=",num1*num2)
print("Division of :",num1,"/",num2,"=",num1/num2)



# ********  Calculator Using IF Else Statement  ********


print("-------- Simple Calculator --------- ")

print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")

op = input("enter operator [1,2,3,4]: ")
if op in ('1', '2', '3', '4'):
    num1 = float(input("enter first number :"))
    num2 = float(input("enter second number :"))
    if op == '1':
        print("Addition of", num1, "+", num2, "=", num1 + num2)
    elif op == '2':
        print("Subtraction of", num1, "-", num2, "=", num1 - num2)
    elif op == '3':
        print("Multiplication of", num1, "*", num2, "=", num1 * num2)
    elif op == '4':
        print("Division of", num1, "/", num2, "=", num1 / num2)
else:
    print("invalid option")
