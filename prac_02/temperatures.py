print("""C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
""")
choice=input("Enter a choice: ").upper()


def main():
    if choice=="C":
        celsius = float(input("Enter temperature in Celsius: "))
        a=converting_Celsius_to_Fahrenheit(celsius)
        print(f"Result: {a:.2f} F")
    elif choice=="F":
        fahrenheit = float(input("Enter temperature in fahrenheit: "))
        b=converting_Fahrenheit_to_Celsius(fahrenheit)
        print(f"Result: {b:.2f} C")
    else:
        print("Invalid choice")

def converting_Celsius_to_Fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def converting_Fahrenheit_to_Celsius(fahrenheit):
    celsius = 5/9*(fahrenheit-32)
    return celsius


main()