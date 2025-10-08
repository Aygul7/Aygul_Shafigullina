"""1. Импортируйте только функции sqrt и pow из модуля math и вычислите:
Квадратный корень из 64
5 в степени 3
Ожидаемый вывод:
8.0
125.0"""
# from math import sqrt, pow
#
# print(sqrt(64))
# print(pow(5, 3))

"""2. Импортируйте модуль random и:
Выведите случайное число от 1 до 10
Выберите случайный элемент из списка [Python, Java, C++]
Ожидаемый вывод:
Случайное число: 7  # (значение может отличаться)
Выбранный язык: Python  # (значение может отличаться)"""
# import random
#
# print(random.randrange(1, 10))
# print(random.choice(['Python', 'Java', 'C++']))


"""3. Создайте свой модуль my_module.py, в котором будут функции:
add(a, b): складывает два числа
multiply(a, b): умножает два числа
Пример вызова в другом файле:
import my_module

print(my_module.add(3, 5))  # 8
print(my_module.multiply(4, 6))  # 24
Cоздайте my_module.py в той же папке!"""
# import my_module
#
# print(my_module.add(3, 5))  # 8
# print(my_module.multiply(4, 6))  # 24


"""4. Создайте два Python-файла:

utils.py – в нем создайте функцию greet(name), которая выводит приветствие.
main.py – в нем импортируйте greet() из utils.py и вызовите её.
Пример вызова в main.py
from utils import greet

greet("Алексей")  # Привет, Алексей!
Запустите main.py и убедитесь, что импорт работает!"""

"""5. Напишите программу, которая измеряет время выполнения кода с помощью time.sleep(2), используя модуль time.
Ожидаемый вывод:
Код выполнялся 2.0001 сек"""
# import time
# from utils import greet
#
# def count_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Время выполнения: {end_time - start_time} сек")
#         return result
#     return wrapper
#
# @count_time
# def func_1():
#     time.sleep(2)
#     greet("Алексей")
#     print('Фунция отработала')
#     return "Возврат из функции"
#
# res = (func_1())
# print(res)


"""6. Напишите код, который делает HTTP-запрос и получает данные с сайта:
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Должно вывести 200"""

# import requests
#
# response = requests.get("https://api.github.com")
# print(response.status_code)


"""7. Установите библиотеку matplotlib и постройте график.
Напишите код:
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

plt.plot(x, y, marker='o')
plt.title("Пример графика")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()"""

# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 50]
#
# plt.plot(x, y, marker='o')
# plt.title("Пример графика")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

"""8. Создайте requirements.txt с зависимостями вашего проекта.
Удалите один из установленных модулей, например requests
Восстановите зависимости с помощью установки из requirements.txt"""
# pip install requests
# pip freeze requirements.txt
# pip uninstall requests
# pip install -r .\requirements.txt
# pip install --upgrade pip

"""9. Создание простого пакета
Создайте пакет math_operations с модулями:
addition.py → Функция add(a, b) складывает 2 числа
subtraction.py → Функция subtract(a, b) вычитает
Структура проекта:

math_operations/
│── __init__.py
│── addition.py
│── subtraction.py
main.py

И запустите обе функции в main.py"""