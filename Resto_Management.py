
menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
    'Briyani':160,
}


print("**************")
print("WELCOME TO MY RESTAURANT")
print("Pizza: Rs40\nPaste: 50\nBurger: 60\nSalad: 70\nCoffee: 80\nBriyani: 160")

total_order = 0

item_1 = input("Enter the name of your item you want to order = ")
if item_1 in menu:
    total_order += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not avaialabe yet!")

another_order = input("Do you want to add another item?(Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter your another item = ")
    if item_2 in menu:
        total_order += menu[item_2]
        print(f"Your item {item_2} has been ordered")
    else:
        print(f"Ordered item {item_2} is not avaialabe yet!")

print(f"The total amount pf items to pay is: {total_order}")#Forward string = print(f" ")       

