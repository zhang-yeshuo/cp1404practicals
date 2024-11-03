from prac_06.guitar import Guitar
def main():
    print("My guitars!")
    guitars = []
    while True:
        name = input("Name: ")
        if name=="":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        my_guitar = Guitar(name, year, cost)
        guitars.append(my_guitar)
        print(f"{my_guitar} added.")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()



