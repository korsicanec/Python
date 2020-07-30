# Написати функцію season, яка приймає 1 аргумент - номер місяця (від 1 до 12), і повертає пору року, якій цей місяць належить (зима, весна, літо або осінь).


def season(month):
    if month < 3 or month  == 12:
        return "Winter"
    if 3 <= month < 6:
        return "Spring"
    if 6 <= month < 9:
        return "Summer"
    if 9 <= month < 12:
        return "Autumn"
b = 1
while b<13:
    print(b)
    print(season (b))
    b+=1
