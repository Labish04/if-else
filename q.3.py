salary=int(input("Pleae enter monthly salary: "))
if salary >= 50000:
    print("Higher Earner")
elif salary <=0:
    print("Please enter positive number.")
elif salary < 50000:
    if salary > 20000:
        print("Mid Earner")
    elif salary <= 20000:
        print("Low Earner")
    else:
        print("Not Classified")
else:
    print("Invalid Input!")