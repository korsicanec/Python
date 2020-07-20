# Задано чотирицифрове натуральне число. 
# Знайти добуток цифр цього числа.
# Записати число в реверсному порядку.

number = 5896
strNumber = str(number)
prodNumber = int(strNumber[0]) * int(strNumber[1]) * int(strNumber[2]) * int(strNumber[3])
print(prodNumber)
reverseNumber = int(strNumber[3]) + int(strNumber[2]) + int(strNumber[1]) + int(strNumber[0])
print(reverseNumber)
