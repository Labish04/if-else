number= int(input("Enter a number: "))
if number%2==0:
    if number%5==0:
        print("Number is divisible by both 2 and 5.")
    else:
        print("Number is divisible by 2.")
else:
    print("Not divisible by 2.")