# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
n = int(input("введите трехзначное число", ))
sum_value = 0
count_it = 0
while n > 0:
    x = n % 10
    sum_value = sum_value + x
    n = n // 10
    count_it += 1
if count_it != 3:
    print('введено не трхзначное число')
else:
    print(sum_value)
