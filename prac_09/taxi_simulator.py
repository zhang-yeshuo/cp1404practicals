from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
current_taxi = None
total_fare = 0
print("Let's drive!")
print("q)uit, c)hoose taxi, d)rive")
option = input(">>> ").lower()
while option != 'q':
    if option == 'c':
        print("Taxis available: ")
        for i, taxi in enumerate(taxis):
            print(f"{i} - {taxi}")
        try:
            taxi_number = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_number]
        except IndexError:
            print("Invalid taxi choice")
    elif option == 'd':
        if current_taxi:
            try:
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print(f"Your trip in the {current_taxi.name} cost ${fare:.2f}")
                total_fare += fare
            except ValueError:
                print("Invalid distance.")
        else:
            print("You must select a taxi before driving.")
    else:
        print("Invalid option.")
    print(f"Bill to date: ${total_fare:.2f}")
    print("q)uit, c)hoose taxi, d)rive")
    option = input(">>> ").lower()
print(f"Total trip cost: ${total_fare:.2f}")
print("Taxis are now:")
for i, taxi in enumerate(taxis):
    print(f"{i} - {taxi}")
