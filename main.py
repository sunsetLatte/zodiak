# Задача "Знаки зодиака"
print ("Знаки зодиака")
month = input("Введите месяц: ")
day = int(input("Введите число: "))

if month == "март":
    if 1 <= day <= 20:
        print("Рыбы")
    elif 21 <= day <= 31:
        print("Овен")

if month == "апрель":
    if 1 <= day <= 20:
        print("Овен")
    elif 21 <= day <= 30:
        print("Телец")

if month == "май":
    if 1 <= day <= 20:
        print("Телец")
    elif 21 <= day <= 31:
        print("Близнецы")

if month == "июнь":
    if 1 <= day <= 21:
        print("Близнецы")
    elif 22 <= day <= 30:
        print("Рак")

if month == "июль":
    if 1 <= day <= 22:
        print("Рак")
    elif 23 <= day <= 31:
        print("Лев")

if month == "август":
    if 1 <= day <= 23:
        print("Лев")
    elif 24 <= day <= 31:
        print("Дева")

if month == "сентябрь":
    if 1 <= day <= 23:
        print("Дева")
    elif 24 <= day <= 30:
        print("Весы")

if month == "октябрь":
    if 1 <= day <= 23:
        print("Весы")
    elif 24 <= day <= 31:
        print("Скорпион")

if month == "ноябрь":
    if 1 <= day <= 22:
        print("Скорпион")
    elif 23 <= day <= 30:
        print("Стрелец")

if month == "декабрь":
    if 1 <= day <= 21:
        print("Стрелец")
    elif 22 <= day <= 31:
        print("Козерог")

if month == "январь":
    if 1 <= day <= 20:
        print("Козерог")
    elif 21 <= day <= 31:
        print("Водолей")

if month == "февраль":
    if 1 <= day <= 20:
        print("Водолей")
    elif 21 <= day <= 30:
        print("Рыбы")
