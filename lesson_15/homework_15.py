"""1. Создайте текстовый файл data.txt со следующим содержимым:

Python – это мощный язык программирования.
Работа с файлами важна для автоматизации.
Чтение файлов в Python удобно и просто.

Напишите программу, которая полностью прочитает файл и выведет его содержимое."""
# with open('data.txt', 'w', encoding='utf-8') as file:
#     file.write("Python – это мощный язык программирования.\n")
#     file.write("Работа с файлами важна для автоматизации.\n")
#     file.write("Чтение файлов в Python удобно и просто.\n")
#
# with open('data.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)


"""2. Напишите программу, которая считает и выведет только первую строку из файла data.txt.
Ожидаемый вывод:
Python – это мощный язык программирования."""
# with open("data.txt", 'r', encoding='utf-8') as file:
#     line = file.readline()
#     print(line)


"""3. Откройте файл data.txt и прочитайте первые 10 символов.
Ожидаемый вывод:
Python – э"""
# with open('data.txt', 'r', encoding='utf-8') as file:
#     content = file.read(10)
#     print(content)

"""4. Прочитайте все строки файла и сохраните их в список. Затем выведите этот список.
Ожидаемый вывод:
['Python – это мощный язык программирования.\n', 'Работа с файлами важна для автоматизации.\n',
 'Чтение файлов в Python удобно и просто.\n']"""
# result = []
# with open ('data.txt', 'r', encoding='utf-8') as file:
#     result = [text for text in file.readlines()]
#     print(result)


"""5. Напишите программу, которая считает строки файла data.txt в цикле и выводит их по одной, 
убирая символ \n в конце.
Ожидаемый вывод:
Строка: Python – это мощный язык программирования.
Строка: Работа с файлами важна для автоматизации.
Строка: Чтение файлов в Python удобно и просто."""
# with open('data.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print("Строка: ", line, end="")

"""6. Откройте файл data.txt, прочитайте 5 символов, затем переместите указатель в начало файла
и снова прочитайте 5 символов и выведите их.
Ожидаемый вывод:
Python
Python"""
# with open('data.txt', 'r', encoding='utf-8') as file:
#     content = file.read(6)
#     print(content)
#     file.seek(0)
#     print(file.read(6))


"""7. Напишите программу, которая откроет файл data.txt, определит его размер (в байтах) и выведет его.
Ожидаемый вывод:
Размер файла: 128 байт  # (значение может отличаться)"""
# with open('data.txt', 'r', encoding='utf-8') as file:
#     file.read()
#     size = file.tell()
#     print(size)

"""8. Используйте with open(), чтобы прочитать и вывести содержимое файла data.txt."""

"""9. Напишите программу, которая пытается открыть файл data.txt, прочитать его содержимое и вывести его.
Если файл не найден, программа должна вывести "Ошибка: Файл не найден".

Ожидаемый вывод (если файл есть):
Python – это мощный язык программирования.
Работа с файлами важна для автоматизации.
Чтение файлов в Python удобно и просто.

Ожидаемый вывод (если файла нет):
Ошибка: Файл не найден"""
# try:
#     f = open('data.txt', 'r', encoding='utf-8')
#     try:
#         text = f.read()
#         print(text)
#     finally:
#         f.close()
#
#
# except FileNotFoundError:
#     print("Файл не найден")

"""10. Модифицируйте программу из Задания 1, добавив гарантированное закрытие файла в блоке finally."""
# f = open(file='data.txt')
# f.close()

"""11. Используйте with open(), чтобы безопасно открыть файл data.txt и прочитать его построчно.
Если файл не найден, выведите "Ошибка: Файл не найден"."""
# try:
#     with open('data.txt', 'r', encoding='utf-8') as file:
#         for line in file:
#             print(line, end='')
# except FileNotFoundError:
#     print("Ошибка: Файл не найден")

"""12. Создайте файл numbers.txt, который содержит по одному числу в каждой строке.
Напишите программу, которая читает файл, суммирует все числа и выводит их сумму.
Если файл не найден, программа должна вывести "Ошибка: Файл не найден"."""
# sum = 0
# try:
#     with open('numbers.txt', 'r', encoding='utf-8') as file:
#         for number in file:
#             sum += int(number)
#     print(sum)
# except FileNotFoundError:
#     print("Ошибка: Файл не найден")

"""13. Создайте файл log.txt.
Программа должна добавлять в него текущую дату и время при каждом запуске.
Используйте модуль datetime и режим "a".

Получение даты и времени для логирования:
import datetime
print(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

Пример содержимого файла после нескольких запусков:

2024-02-16 14:30:01 Запуск программы
2024-02-16 14:35:15 Запуск программы
2024-02-16 14:40:22 Запуск программы"""

import datetime

with open("log.txt", "w", encoding='utf-8') as file:
    file.write(f'{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")} Запуск программы\n')
    file.write(f'{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")} Запуск программы\n')
    file.write(f'{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")} Запуск программы\n')
