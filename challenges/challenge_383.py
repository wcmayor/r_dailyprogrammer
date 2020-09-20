# https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/

import requests
from collections import defaultdict

def same_necklace(first, second):
    return len(first) == len(second) and second in first + first

def repeats(string):
    if len(string) == 0:
        repetitions = 1
    else:
        repetitions = 0
    for counter in range(len(string)):
        if string == string[counter:] + string[:counter]:
            repetitions += 1
    return repetitions

def normalize(seq):
    return min(seq[d:] + seq[:d] for d in range(len(seq)))

def index(wordlist):
    to_return = defaultdict(list)
    
    for word in wordlist:
        to_return[normalize(word)].append(word)
    
    return to_return

def bonus2(listUrl):
    wordlist = requests.get(listUrl).text.splitlines()
    return max(index(wordlist).values(), key=len)

def main():
    print(same_necklace("nicole", "icolen"))
    print(same_necklace("abc", "cba"))
    print(repeats("abcabcabc"))
    print(bonus2("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt"))

if __name__ == "__main__":
    main()