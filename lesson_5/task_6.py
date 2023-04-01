# Задание 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.
def guess_number(ran, x, i=0):
    if i == 10:
        return print(f'вы проиграли ( . Загаданное число {ran}')
    else:
        if ran > x:
            print(ran)
            x = int(input('загаданное число больше '))
            return guess_number(ran,x, i + 1)
        elif ran < x:
            print(ran)

            x = int(input('загаданное число меньше '))
            return guess_number(ran,x, i + 1)
        else:
            return print(f'вы победили! загаданное число {ran}')


from random import randint

num = randint(0, 101)

try:
    n = int(input('отгадайте число от 1 до 100: '))
except:
    print('вы ввели не число!')
guess_number(num, n)