def main():
    get_password()


def get_password():
    name = input("Enter your name: ")
    length = len(name)
    for i in range(length):
        print("*", end="")

main()