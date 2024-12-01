import csv

def main():
    filename = "wimbledon.csv"
    data = read_csv_file(filename)
    champions = get_champions(data)
    countries = get_countries(data)
    display_champions(champions)
    display_countries(countries)

def read_csv_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        data = [row for row in reader]
    return data


def get_champions(data):
    champions = {}
    for row in data:
        champion = row[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def get_countries(data):
    countries =[]
    for row in data:
        country = row[1]
        countries.append(country)
    return sorted(countries)


def display_champions(champions):
    print("Wimbledon Champions: ")
    for champion, count in sorted(champions.items()):
        print(f"{champion} {count}")


def display_countries(countries):
    print("These", len(countries), "countries have won Wimbledon: ")
    print(",".join(countries))





main()