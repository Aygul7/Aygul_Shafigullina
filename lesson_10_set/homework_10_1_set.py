"""1. Создайте множество с элементами .
Добавьте в него число, затем попробуйте добавить уже существующий элемент.
Выведите итоговое множество."""
# set_1 = {15, 26, 53, 97, 88, 256}
# set_1.add('7')
# print(set_1)
# set_1.update('7')
# print(set_1)

"""2. Создайте множество из списка городов:
Выведите его на экран.
Сколько уникальных городов в этом списке?"""
# cities = {'Москва', 'Казань', 'Екатеринбург', 'Иркутск', 'Москва', 'Уфа'}
# print(cities)
# print(len(cities))

"""3. Создайте множество с числами от 1 до 10.
Удалите из него:
Число 5 (если оно есть).
Число 15 (используйте метод, который не вызовет ошибку).
Выведите итоговое множество."""
# nums = set(range(1, 10))
# print(nums)
# nums.discard(5)
# print(nums)
# nums.discard(15)
# print(nums)

"""4. Преобразуйте строку "abrakadabra" в множество символов.
Выведите итоговое множество и определите, сколько различных букв в слове."""
# a = "abrakadabra"
# b = set(a)
# print(b)
# print(len(b))

"""5. Создайте пустое множество и попробуйте добавить в него следующие элементы:
Число 10
Строку "hello"
Кортеж (1, 2, 3)
Список [4, 5, 6]
Какие из элементов нельзя добавить в множество? Почему?"""
# a = set()
# a.add('10')
# print(a)
# a.add('hello')
# print(a)
# a.add((1, 2, 3))
# print(a)
# a.add([4, 5, 6])
# print(a)
# # нельзя добавить список, т.к. список - изменяемый тип данных. Множество - неизменяемый тип

"""6. Создайте 2 множества, в которых совпадают 2 элемента
Найдите:
Пересечение A и B.
Объединение A и B.
Разность A - B.
Разность B - A.
Симметричную разность A ^ B."""
# A = {1, 6, 33, (1, 2, 3), 'hello'}
# B = {55, 24, 97, (1, 2, 3), 'python'}
# print(A)
# print(B)
# res = A & B
# res = A.intersection(B)
# A &= B
# print(res)
#
# res_2 = A | B
# res_2 = A.union(B)
# A |= B
# print(res_2)
#
# res_3 = A - B
# res_3 = A.difference(B)
# A -= B
# print(res_3)
#
# res_4 = B - A
# res_4 = B.difference(A)
# B -= A
# print(res_4)
#
# res_5 = A ^ B
# res_5 = A.symmetric_difference(B)
# A ^= B
# print(res_5)

"""7. Создайте два множества из чисел 1 до 10:
even_numbers — содержит четные числа.
odd_numbers — содержит нечетные числа.
Проверьте:
Какое будет пересечение &?
Какое будет объединение |?"""
# even_numbers = set()
# odd_numbers = set()
# for i in range(1, 10):
#     if i%2 ==0:
#         even_numbers.add(i)
#     else:
#         odd_numbers.add(i)
#
# print(even_numbers)
# print(odd_numbers)
#
# res_1 = even_numbers & odd_numbers
# res_2 = even_numbers | odd_numbers
# print(res_1)
# print(res_2)

"""8. Даны множества студентов, записавшихся на курсы:
python_students = {"Анна", "Иван", "Мария", "Сергей"}
java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
Определите:
Кто записан на оба курса?
Кто записан только на один курс?
Кто записан хотя бы на один курс?"""
# python_students = {"Анна", "Иван", "Мария", "Сергей"}
# java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
# both_courses = python_students & java_students
# print(both_courses)
# one_course_python = java_students - python_students
# print(one_course_python)
# one_course_java = python_students - java_students
# print(one_course_java)
# one_course_java_python = one_course_java |one_course_python
# print(one_course_java_python)

"""9. Даны множества слов:
text1 = set("программирование")
text2 = set("автоматизация")
Найдите общие буквы в двух словах.
Найдите буквы, которые есть только в первом слове.
Найдите уникальные буквы каждого слова."""
# text1 = set("программирование")
# text2 = set("автоматизация")
# common_letters = text1 | text2
# print(common_letters)
# text1_letters = text1-text2
# print(text1_letters)
# print(text1)
# print(text2)

