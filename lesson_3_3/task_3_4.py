# 4. Реализовать функцию my_func(), которая принимает три позиционных
# аргумента,и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()

def exe_3(a, b, c):
    z = [a, b, c]
    # z.remove(min(a, b, c))
    z.sort()
    # return sum(z)
    return z[1] + z[2]


def exe_3_use():
    print(exe_3(3, 6, 7))


exe_3_use()

# решение подсмотрено в и-нете.т.к. мое никак не работает. это тоже не нравится.
# не понимаю как сделать так чтобы значение вносил пользователь? через переменную
# список заполняется кортежами... Всю голову сломала...пожалуйст подскажите

# num_1 = int(input(('введите первое число: '), )),
# num_2 = int(input(('введите второе число: '), )),
# num_3 = int(input(('введите третье число: '), )),


# def my_func(n_1,n_2,n_3):
#     list_1 = [n_1,n_2,n_3]
#     # list_1.sort()
#     # return list_1[1] + list_1[2]
#     min_value = min(list_1)
#     return sum(list_1) - min_value
# print(f'сумма наибольших двух чисел = {my_func(num_1,num_2,num_3)}')
