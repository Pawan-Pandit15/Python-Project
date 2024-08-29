print("Welcome to Apna Hotel")
menu = {
    "Tea": 10,
    "Coffe": 20,
    "Veg Thali": 50,
    "Non veg Thali": 70
}

print("Tea :10\nCoffe :20\nVeg Thali :50\nNon veg Thali :70")
total_order_price = 0
item1 = input("Enter your first order: ")
if item1 in menu:
    print("your fisrt order complete Successfully")
    total_order_price += menu[item1]

else:
    print("This item Not Available")

another_order = input("order another order (Yes/No): ")
if another_order == "Yes":
    item2 = input("enter second order: ")
    if item2 in menu:
        print("your second order complete Sucessfully")
        total_order_price += menu[item2]
    else:
        print("This item is not Available in Menu")
else:
    print("Thank you for order in Apna Heltel")

print("Your Total Payble Amount", total_order_price)