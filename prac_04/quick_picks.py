
from random import randint
def main():
    quick_pick=int(input("How many quick picks? "))
    for i in range(quick_pick):
        find_random_number(quick_pick)

def find_random_number(quick_pick):
    CONSTANTS = []
    for i in range(quick_pick):
        random_number = randint(1, 45)
        if random_number not in CONSTANTS:
            CONSTANTS.append(random_number)
        else:
            while random_number in CONSTANTS:
                random_number = randint(1, 45)
            CONSTANTS.append(random_number)
        CONSTANTS = sorted(CONSTANTS)
    for number in CONSTANTS:
        print(number, end=" ")
    print()

main()

