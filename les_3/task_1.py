# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
#
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень
list_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_1 = int(input('введите число от 1 до 12 ', ))
if month_1 == list_months[0] or month_1 == list_months[2] or month_1 == \
        list_months[
            11]:
    print('winter')
elif month_1 == list_months[3] or month_1 == list_months[4] or month_1 == \
        list_months[5]:
    print('spring')
elif month_1 == list_months[6] or month_1 == list_months[7] or month_1 == \
        list_months[8]:
    print('summer')
else:
    print('autumn')
dictionary_year = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring',
                   5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer',
                   9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
month = int(input('введите число от 1 до 12 ', ))
print(dictionary_year[month])
