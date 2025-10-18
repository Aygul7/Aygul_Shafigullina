"""1. Оставь только строки и списки из списка:
items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
Ожидаемый результат:
['hello', [1, 2], 'world']"""
from operator import truediv

# items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
# new_item = []
# for item in items:
#     if isinstance(item, (list, str)):
#         new_item.append(item)
#
# print(new_item)


"""2. Создай функцию describe_type(x), которая:
печатает "Это строка", если x — строка
"Это число", если x — int или float
"Это булевое значение", если x — bool
"Неизвестный тип" — в остальных случаях
Пример вызова:
describe_type(5.5)       # Это число
describe_type(True)      # Это булево значение
describe_type("Привет")  # Это строка
describe_type([1, 2, 3]) # Неизвестный тип"""

# def describe_type(x):
#     if isinstance(x, str):
#         print("Это строка")
#     elif isinstance(x, bool):
#         print("Это булевое значение")
#     elif isinstance(x, (int, float)):
#         print("Это число")
#     else:
#         print("Неизвестный тип")
#
# describe_type(5.5)       # Это число
# describe_type(True)      # Это булево значение
# describe_type("Привет")  # Это строка
# describe_type([1, 2, 3]) # Неизвестный тип"

"""3. Создай функцию filter_list(f, data: list[int]) -> list[int],
которая возвращает только те элементы из data, которые проходят проверку функцией f.
Проверь на функции lambda x: x > 3 и списке [1, 3, 5, 7]."""
# def filter_list(f, data: list[int]) -> list[int]:
#     return [x for x in data if f(x)]
#
# # Проверка на функции lambda x: x > 3 и списке [1, 3, 5, 7]
# result = filter_list(lambda x: x > 3, [1, 3, 5, 7])
# print(result)  # [5, 7]

"""4. Добавь аннотацию типов в следующую функцию и укажи, что она возвращает None:
def print_info(name, age, tags):
    print(name, age, tags)"""
# def print_info(name: str, age: int, tags: list) -> None:
#     print(name, age, tags)
#
#
# print_info('Maria', 25, ['qa'] )


"""5. Создай функцию def analyze(data),
которая выводит количество элементов и среднее значение, если список не пустой."""
# def analyze(data):
#     if not data:  # если список пустой
#         print("Список пустой")
#     else:
#         count = len(data)
#         average = sum(data) / len(data)
#         print(f"Количество элементов: {count}, Среднее значение: {average}")
#
# analyze([1, 2, 3])

"""6. Список логических значений:
flags = [True, True, True, False]
Проверь:
Все ли значения истинные
Есть ли среди них хотя бы одно истинное
Ожидаемый результат:
False
True"""
# flags = [True, True, True, False]
# print(all(flags))
# print(any(flags))

"""7. Поле в игре "Крестики-нолики" представлено так:
field = ['x', 'x', 'x', 'o', 'o', '', '', '', '']
Проверь, победил ли 'x' по первой строке.
Ожидаемый результат:
True"""
# field = ['x', 'x', 'x', 'o', 'o', '', '', '', '']
# result = field[0] == field[1] == field[2] == 'x'
# print(result)

"""8. На поле для "Сапёра" находится мина, если в ячейке символ *. Есть ли мина?
P = ['0', '0', '0', '*', '0']
Ожидаемый результат:
True"""
# P = ['0', '0', '0', '*', '0']
# # result = False
# # for cell in P:
# #     if cell == '*':
# #         result = True
# #         break
# # print(result)
#
# # решение с any()
# result = any(cell == '*' for cell in P)
# print(result)

"""9. Выбери случайное значение из списка:
colors = ["red", "green", "blue", "yellow", "purple"]
Ожидаемый результат:
Выбран цвет: blue"""
# import random
#
#
# colors = ["red", "green", "blue", "yellow", "purple"]
# choice = random.choice(colors)
# print(choice)

"""10. Сгенерируй 10 случайных чисел от 0 до 100 и выведи их. 
Сделай так, чтобы результат был одинаковый при каждом запуске."""
# import random
#
# random.seed(42)  # можно использовать любое число
#
# numbers = [random.randint(0, 100) for _ in range(10)]
# print(numbers)

"""Напиши функцию greet(), которая принимает строку name и возвращает строку Привет, <name>!.
Добавь аннотацию типов.
Ожидаемый вывод:
Привет, Анна!"""

# def greet(name: str):
#     print(f"Привет, {name}!")
#
# result = greet("Anna")


"""12. Создай функцию multiply(a, b), которая принимает два числа int или float и возвращает их произведение.
Добавь аннотацию типов.
Ожидаемый вывод:
20"""
# def multiply(a: int | float, b: int | float) -> int | float:
#     return a * b
#
# result = multiply(15, 2.8)
# print(result)


"""13. Проверь типы аргументов функции через __annotations__.
Создай функцию area(length: float, width: float) -> float и распечатай её аннотации.
Ожидаемый вывод:
{'length': <class 'float'>, 'width': <class 'float'>, 'return': <class 'float'>}"""
# def area(length: float, width: float) -> float:
#     return length * width
#
# print(area.__annotations__)
