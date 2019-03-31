from random import randint

#generate a random number
def rand_num(min, max):
    return randint(min, max)

#simulate roll action
#takes the die type as well as the number of that die
def roll(type, amount):
    for die in range(amount):
        print(rand_num(1, type))

#get die type
print("What die would you like to roll? (20,12,10,8,6,4)")
die_type = int(input("D: "))

#get amount
print(f"How many D{die_type}'s would you like to roll? ")
die_amount = int(input("Amount: "))

#call roll w/ user input
roll(die_type, die_amount)
