# https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/
import csv

def tax(income):
    if not isinstance(income, int) and not isinstance(income, float):
        raise ValueError("Income must be an integer or float.")

    if income > 100000000:
        raise ValueError("Income must be less than or equal to 100,000,000.")

    taxAmt = 0

    with open('challenges/challenge_379_input.csv') as inputfile:
        taxBrackets = csv.DictReader(inputfile, quoting=csv.QUOTE_NONNUMERIC)
        lastCap = 0

        for bracket in taxBrackets:
            if bracket['cap'] == '' or income < bracket['cap']:
                bracket['cap'] = income
            
            taxAmt += (bracket['cap'] - lastCap) * bracket['rate']
            
            if bracket['cap'] == income:
                break
            
            lastCap = bracket['cap']
    return int(taxAmt)