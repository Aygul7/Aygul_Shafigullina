"""1. Создайте множество из квадратов чисел от 1 до 10, но только для четных чисел."""
set_a = {x ** 2 for x in range(1, 10) if x % 2 == 0}
print(set_a)


"""2. Дан список:
words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
Создайте множество уникальных слов, преобразовав их в верхний регистр."""
# words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
# words_set = {x.upper() for x in words}
# print(words_set)


"""3. Дан словарь:
grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
Используя генератор, создайте новый словарь, где:
Если оценка больше или равна 80, записать "отлично".
Если меньше 80, записать "удовлетворительно"."""
# grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
# grades_new = {name: "отлично" if grade >= 80 else "удовлетворительно"
#           for name, grade in grades.items()}
#
# print(grades_new)


"""4. Дано множество слов:
text = {"Python", "automation", "programming", "testing"}
Создайте новый словарь, где ключи – это слова из множества, а значения – длина каждого слова."""
# text = {"Python", "automation", "programming", "testing"}
# new_dict = {name:len(name) for name in text}
# print(new_dict)


"""5. Создайте вложенный словарь, где ключи – числа от 1 до n (для примера пусть n = 10), 
а значения – множества квадратов чисел от 1 до ключа.
Пример для n = 3:
{
1: {1},
2: {1, 4},
3: {1, 4, 9}
}"""
n = 10
result = {i: {x*x for x in range(1, i+1)} for i in range(1, n+1)}

print(result)