# https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/

def balanced(str_to_check):
    x = 0
    y = 0

    for char in str_to_check:
        if char == "x":
            x += 1
        elif char == "y":
            y += 1
        else:
            continue

    return x == y

def balanced_bonus(str_to_check):
    results = {}

    for char in str_to_check:
        if char in results.keys():
            results[char] += 1
        else:
            results[char] = 1
    last_found = 0
    balanced = True
    for char, count in results.items():
        if last_found == 0:
            last_found = count
        if count != last_found:
            balanced = False

    return balanced