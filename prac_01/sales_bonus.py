"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
bonus=0
while sales>0:
    if sales<1000:
        bonus=sales*0.1
        print(f"bonus: {bonus}")

    elif sales>=1000:
        bonus=sales*0.15
        print(f"bonus: {bonus}")

600
sales = float(input("Enter sales: $"))


