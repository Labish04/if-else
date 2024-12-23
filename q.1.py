price=int(input("Enter the frice of an item:"))
if price>=1000:
    discount= 0.1*price
    final_price= price - discount
    print("Your final price is {}".format(final_price))
elif price>=500:
    discount= 0.05*price
    final_price= price- discount
    print("Your final price is {}".format(final_price))
else:
    print("Discount not applied")