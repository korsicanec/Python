# Написати функцію is_year_leap, приймає 1 аргумент - рік, і повертає True, якщо рік високосний, і False в іншому випадку.


def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False
