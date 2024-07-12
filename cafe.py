# Defining the menue of the cafe

menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad' :70,
    'Cofee' :80
}

#Greet to customer
print("Welcome to KAMAL Cafe")

# Displaying the menue to the customer
for key in menu:
    print(key,":-",menu[key])
bill = 0 
while True:
    order = input("Please enter the item OR type DONE to End : ")
    if order== "DONE":
        break

    elif order in menu:
        quantity=int(input("Enter the quantity"))
        bill = bill + (menu[order]*quantity)

    else:
        print(" Sorry! this Item is not available plese enter correct item : ")

print("Your bill", bill)
print("Bill with GST =",bill + (bill*(18/100)))
