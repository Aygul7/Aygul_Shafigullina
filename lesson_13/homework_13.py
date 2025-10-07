"""1. Напишите декоратор uppercase_decorator, который делает результат выполнения функции прописными буквами.
Пример вызова:
@uppercase_decorator
def say_hello():
    return "hello, world!"
print(say_hello())  # "HELLO, WORLD!"""

# def uppercase_decorator(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs).upper()
#     return wrapper
#
# @uppercase_decorator
# def say_hello():
#     return "hello, world!"
# print(say_hello())

"""2. Создайте декоратор repeat(n), который выполняет функцию n раз.
Пример вызова:
@repeat(3)
def hello():
    print("Hello!")
hello()
Вывод:
Hello!
Hello!
Hello!"""

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @repeat(3)
# def hello():
#     print("Hello!")
# hello()


"""3. Создайте декоратор cache, который кэширует результаты выполнения функции.
Если функция вызывается с теми же аргументами – возвращать сохраненный результат вместо нового вычисления.
Пример вызова:
@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b
print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
print(slow_add(2, 3))  # 5 (результат взят из кэша)"""


# def cache(func):
#     cached_results = {}  # Словарь для хранения результатов
#
#     def wrapper(*args, **kwargs):
#         # Создаем ключ на основе аргументов
#         key = (args, tuple(kwargs.items()))
#
#         # Если результат уже в кэше - возвращаем его
#         if key in cached_results:
#             return cached_results[key]
#
#         # Иначе вычисляем и сохраняем в кэш
#         result = func(*args, **kwargs)
#         cached_results[key] = result
#         return result
#
#     return wrapper
#
#
# # Пример использования
# @cache
# def slow_add(a, b):
#     print(f"Вычисляю {a} + {b}...")
#     return a + b
#
#
# print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
# print(slow_add(2, 3))  # 5 (результат взят из кэша)
# print(slow_add(3, 2))  # "Вычисляю 3 + 2..." 5 (другой порядок аргументов)


"""4. Создайте декоратор с таймером timer(repeat), который выполняет функцию repeat раз и выводит среднее время выполнения.
Пример вызова:
@timer(3)
def slow_function():
    time.sleep(1)
slow_function()  # Среднее время выполнения: 1.0002 сек"""
import time


def timer(repeat):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            results = []

            for i in range(repeat):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()

                execution_time = end_time - start_time
                total_time += execution_time
                results.append(result)

                print(f"Попытка {i + 1}: {execution_time:.4f} сек")

            average_time = total_time / repeat
            print(f"Среднее время выполнения: {average_time:.4f} сек")
            print(f"Количество повторений: {repeat}")

            return results  # Возвращаем список всех результатов

        return wrapper

    return decorator


# Пример с функцией, возвращающей значение
@timer(3)
def calculate_square(x):
    time.sleep(0.5)
    return x * x


results = calculate_square(5)
print(f"Результаты: {results}")


# другой вариант с определением общего времени выполнения- комбинированы 2 декоратора
# def count_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Время выполнения: {end_time - start_time} сек")
#         return result
#     return wrapper
#
# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @count_time
# @repeat(3)
# def hello():
#     print("Hello!")
# hello()