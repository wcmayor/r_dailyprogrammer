# https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/

import re
from random import randint

def roll_dice(dice, display_rolls=False):
    rolls_min = 1
    rolls_max = 100
    sides_min = 2
    sides_max = 100

    rolls = []

    if not re.match(r'^\d+d\d+$', dice):
        raise ValueError("Input dice string does not match the required pattern!")

    number_of_rolls = int(dice[:dice.index('d')])
    number_of_sides = int(dice[dice.index('d') + 1:])

    if number_of_rolls not in range(rolls_min, rolls_max + 1):
        raise ValueError("Input dice has an invalid value for the number of roles (" + str(number_of_rolls) + ") "\
            "Expected value between " + str(rolls_min) + " and " + str(rolls_max) + " (inclusive)")
    if number_of_sides not in range(sides_min, sides_max + 1):
        raise ValueError("Input dice has an invalid value for the number of sides. (" + str(number_of_sides) + ") "\
            "Expected value between " + str(sides_min) + " and " + str(sides_max) + " (inclusive)")

    while number_of_rolls > 0:

        rolls.append(randint(1, number_of_sides))
        number_of_rolls -= 1
    
    if display_rolls:
        return str(sum(rolls)) + ": " + " ".join(map(str, rolls))
    
    else:
        return sum(rolls)