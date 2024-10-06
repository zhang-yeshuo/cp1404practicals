# 1.
name = input("Please enter your name: ")
file = open("name.txt", "w")
print(name, file=file)
file.close()

# 2.
file = open("name.txt", "r")
name = file.read()
file.close()
print(f"Hi {name}!")

# 3.
with open("numbers.txt", "r") as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
result = num1 + num2
print(result)

# 4.
with open("numbers.txt", "r") as file:
    for line in file:
        print(line)
