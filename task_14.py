# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k),не превосходящие числа N.
n = int(input('введите крайнюю степень '))
i = 0
while 2 ** i <= n:
    print(f"число 2 в {i} степени = {2 ** i}")
    i += 1
