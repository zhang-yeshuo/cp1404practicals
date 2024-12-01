import csv
from guitar import Guitar


def main():
    guitars = load_guitars("guitars.csv")
    guitars.sort()
    display_guitars(guitars)

    add_guitars(guitars)
    write_guitars("guitars.csv", guitars)



def load_guitars(filename):
    guitars = []
    with open(filename, "r") as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars



def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def add_guitars(guitars):
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))


def write_guitars(filename, guitars):
    with open(filename, "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == "__main__":
    main()
