#Create a file called loops.py and add the following for loop that displays all the odd numbers between1 and 20 with a space between each one.
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a. count in 10s from 0 to 100
for i in range(0,101,10):
    print(i, end=" ")
print()

#b. count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.
stars=int(input("Enter number of stars: "))
for i in range(1,stars+1):
    print("*",end="")
print()

#d. print n lines of increasing stars. Using the same number as above, print lines of increasing stars, starting at 1 with no blank line.
stars=int(input("Enter number of stars: "))
a=1
while a<= stars:
    for i in range(1,a+1):
        print("*",end="")
    print()
    a=a+1



