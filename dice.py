import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes":
    print("Rolling the dices")
    print("the value on the dice are")
    print(random.randint(min, max))
    print (random.randint(min, max))

    roll_again = input("roll the dices again")
