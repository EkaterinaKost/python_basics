# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
n = int(input('введите колличество элементов массива: '))

from random import randint

my_list = [randint(-10, 10) for i in range(n)]
print(*my_list)
x = int(input('введите искомое число : '))
my_list.sort()
print(*my_list)
if my_list[0] == x:
    print(
        f'самое близкое к числу {x} по величине число : {my_list[1]}')
if my_list[n - 1] == x:
    print(
        f'самое близкое к числу {x} по величине число : {my_list[n - 2]}')
for el in range(1, n - 1):
    if my_list[el] == x:
        if abs(my_list[el - 1] - x) < abs(my_list[el + 1] - x):
            print(
                f'самое близкое к числу {x} по величине число : {my_list[el - 1]}')
        elif abs(my_list[el - 1] - x) == abs(my_list[el + 1] - x):
            print(
                f'число : {my_list[el - 1]} и число : {my_list[el + 1]} '
                f'одинаково близки к числу {x} ')
        else:
            print(
                f'самое близкое к числу {x} по величине число : {my_list[el + 1]}')
