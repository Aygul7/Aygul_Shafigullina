"""1. Создайте функцию multiply_by(n), которая принимает число n и возвращает вложенную функцию.
Вложенная функция должна принимать число x и возвращать его произведение на n.
Пример вызова:
times3 = multiply_by(3)
times5 = multiply_by(5)

print(times3(10))  # 30
print(times5(10))  # 50"""

# def multiply_by(n):
#     def multiply(x):
#         return x * n
#
#     return multiply
#
# times3 = multiply_by(3)
# times5 = multiply_by(5)
#
# print(times3(10))  # 30
# print(times5(10))  # 50


"""2. Напишите функцию counter(start=0), которая возвращает вложенную функцию.
Каждый вызов вложенной функции должен увеличивать счетчик на 1.
Пример вызова:

c1 = counter(5)
c2 = counter()

print(c1())  # 6
print(c1())  # 7
print(c2())  # 1
print(c2())  # 2

Подсказка: используйте nonlocal"""


def counter(start=0):
    count = start

    def inner():
        nonlocal count
        count += 1
        return count

    return inner

c1 = counter(5)
c2 = counter()

print(c1())  # 6
print(c1())  # 7
print(c2())  # 1
print(c2())  # 2