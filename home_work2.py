# Задана вага в грамах. Визначити вагу в тонах і кілограмах.

weight = int(input("please enter weight in grams"))
print("you entered: ", weight, "in tonn: ", weight/1000000, "in kilos: ", weight/1000)

# Відомий обсяг інформації в байтах. Перевести в кілобайти, мегабайти.

bytes = int(input ("please enter data in bytes"))
print ("you entered bytes: ", bytes, "in kilobytes: ", bytes/1024, "in megabytes: ", bytes/1048576)

# Користувач вводить два числа. Одне присвоюється одній змінній, а друге - іншій. 
# Необхідно поміняти значення змінних так, щоб значення першої виявилося в другій, а другої - у першій.

a = int(input("enter first number"))
b = int(input("enter second number"))
a, b = b, a

# Обчислити площу і периметр прямокутника за заданими шириною і висотою.

sideA = int(input("Длина: "))
sideB = int(input("Ширина: "))
area = sideA * sideB;
print("Площадь прямоугольника: ", area)

sideA = int(input("Длина: "))
sideB = int(input("Ширина: "))
perimeter = (sideA + sideB) * 2;
print("Периметр прямоугольника: ", perimeter)

