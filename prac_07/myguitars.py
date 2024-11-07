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
        reader = csv.reader(file)
        for line in reader:
            name, year, cost = line
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
    with open(filename, "w",newline="") as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()
