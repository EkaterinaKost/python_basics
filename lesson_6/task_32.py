# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

my_list = [randint(-10, 10) for i in range(11)]
print(*my_list)

min_number = int(input('введите min значение списка: '))
max_number = int(input('введите max значение списка: '))

for i in range(len(my_list)):
    if min_number <= my_list[i] <= max_number:
        print(i, end=' ')
