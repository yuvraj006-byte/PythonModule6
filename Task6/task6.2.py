import random

user_input = int(input("Enter the number of sides the dice has: "))
def die_roll():
    if user_input <= 0:
        print("Sorry, a dice can not have negative sides")
        breakpoint()
    return random.randint(1, user_input)

def die_roll_six():
    while True:
        roll = die_roll()
        print(roll)
        if roll == user_input:
            breakpoint()
            break

die_roll_six()