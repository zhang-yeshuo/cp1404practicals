number=int(input("Number of items: "))
price1=0
if number>=0:
    for i in range(1, number + 1):
        price = float(input("Price of item: "))
        price1 = price + price1
    if price1>100:
        print(f"Total price for {number} items is ${price1*0.9:.2f}  ")
    else:
        print(f"Total price for {number} items is ${price1:.2f}  ")
else:
    print("Invalid number of items!")
