food=(input("Are you vegitarian or non-vegitarian: ")).lower()
if food== "vegitarian":
    choice=str(input("Do you want Salad or Pasta: ")).lower()
    if choice== "salad":
        print("Your choice is {}.".format(choice))
        print("Your order will be ready soon.")
    elif choice== "pasta":
        print("Your choice is {}.".format(choice))
        print("Your order will be ready soon.")
    else:
        print("Not aviable")
elif food== "non-vegitarian":
    choice=(input("Do you want Chicken or Fish: ")).lower()
    if choice== "chicken":
        print("Your choice is {}.".format(choice))
        print("Your order will be ready soon.")
    elif choice=="fish":
        print("Your choice is {}.".format(choice))
        print("Your order will be ready soon.")
    else:
        print("Not avaible")
else:
    print("Invalid answer!")