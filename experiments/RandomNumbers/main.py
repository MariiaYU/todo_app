import random

while True:
    lower_bound = int(input("Enter a lower bound: "))
    upper_bound = int(input("Enter an upper bound: "))

    #random_num = random.randint(lower_bound, upper_bound)
    rand = random.randrange(lower_bound, upper_bound + 1)

    #print("The random number is: " + str(random_num))
    print(rand)