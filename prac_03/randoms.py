import random
for i in range(100):
    print(random.randint(5, 20))
    # The smallest number is 5 and the largest number is 20

for i in range(100):
    print(random.randrange(3, 10, 2))
    # The smallest number is 3, the largest number is 9
    # This cannot produce a 4

for i in range(100):
    print(random.uniform(2.5, 5.5))
    # The number are all floats
    # The largest number is 5.5 and the smallest number is 2.5


# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1,100))