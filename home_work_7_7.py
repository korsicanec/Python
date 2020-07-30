# Написати функцію date, яка приймає 3 аргументи - день, місяць і рік. Повернути True, якщо така дата є в нашому календарі, і False - в іншому випадку.

def date(day, month, year):
    day_in_month = {1: 31,
                    2: 29 if is_year_leap(year) else 28,
                    3: 31,
                    4: 30,
                    5: 31,
                    6: 30,
                    7: 31,
                    8: 31,
                    9: 30,
                    10: 31,
                    11: 30,
                    12: 31}

    if 1 <= month <= 12 and 1 <= day <= day_in_month[month]:
        return True
    return False