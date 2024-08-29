
house_rent = int(input("Enter Total House Rent = "))
food = int(input("Enter Total Food Expense = "))
electricity_bill_unit = int(input("Enter Electricity Spend Unit = "))
electricity_per_unit = int(input("Enter Electricity Per Unit Cost = "))
persons = int(input("Enter Total Person = "))

total_electricity_bill = electricity_bill_unit * electricity_per_unit

total_expense = (house_rent + food + total_electricity_bill)

print("Each Persons Will Pay",total_expense/persons)
