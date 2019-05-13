# https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/

def sum_of_digits(number):
    
    sum_of_digits = 0
    
    while number:
        sum_of_digits += number % 10
        number //= 10
    
    return sum_of_digits

def getAdditivePersistence(number):
    additive_persistence = 0

    while number >= 10:
        number = sum_of_digits(number)
        additive_persistence += 1
    
    return additive_persistence

if __name__ == "__main__":
    assert(getAdditivePersistence(13) == 1)
    assert(getAdditivePersistence(1234) == 2)
    assert(getAdditivePersistence(9876) == 2)
    assert(getAdditivePersistence(199) == 3)