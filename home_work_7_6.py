# Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000, і повертає True, якщо воно просте, і False - в іншому випадку.

def is_prime(number):
    if number == 1:
        return False
    for possible_divisor in range(2, number):
        if number % possible_divisor == 0:
            return False
    return True
