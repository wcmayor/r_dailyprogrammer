# https://www.reddit.com/r/dailyprogrammer/comments/dv0231/20191111_challenge_381_easy_yahtzee_upper_section/

from collections import Counter

import requests

def yahtzee_upper(rolls):
    return int(max(dice * occurrences for dice, occurrences in Counter(rolls).items()))

def yahtzee_upper_large():
    numbers = requests.get("https://gist.githubusercontent.com/cosmologicon/beadf49c9fe50a5c2a07ab8d68093bd0/raw/fb5af1a744faf79d64e2a3bb10973e642dc6f7b0/yahtzee-upper-1.txt").text.splitlines()
    return yahtzee_upper(numbers)