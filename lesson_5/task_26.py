# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
def a_degree_b(a, b, i=1, product=1):
    if i == b + 1:
        return print(f'{a}  в степени {b} = {product}')
    else:
        product = product * a
        i += 1
        return a_degree_b(a, b, i, product)


try:
    first = int(input('введите число: '))
    second = int(input('введите число: '))
except:
    print('вы ввели не число!')

a_degree_b(first, second)
