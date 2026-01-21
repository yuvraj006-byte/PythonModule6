import random

def die_roll():
    return random.randint(1,6)

def die_roll_six():
    while True:
        roll = die_roll()
        print(roll)
        if roll == 6:
            breakpoint()
            break

die_roll_six()