# https://www.reddit.com/r/dailyprogrammer/comments/aphavc/20190211_challenge_375_easy_print_a_new_number_by/

def incrementEachDigit(number):
    output = ""

    for digit in map(int, str(number)):
        output += str(digit + 1)

    return int(output)

if __name__ == "__main__":
    print(str(incrementEachDigit(998)))
    print(str(incrementEachDigit(678)))