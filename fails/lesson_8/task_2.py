'''Задание на закрепление знаний по модулю json. Есть файл orders в формате
JSON с информацией о заказах. Написать скрипт, автоматизирующий его
заполнение данными. Для этого: Создать функцию write_order_to_json(),
в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна
предусматривать запись данных в виде словаря в файл orders.json. При записи
данных указать величину отступа в 4 пробельных символа; Проверить работу
программы через вызов функции write_order_to_json() с передачей в нее
значений каждого параметра.
'''
import json


def write_order_to_json(item, quantity, price, buyer, date):
    order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    with open('orders.json', 'w') as f:
        json.dump(order, f, indent=4)


write_order_to_json(
    item=['принтер', 'монитор', 'сканер'],
    quantity=[2, 4, 2],
    price=[15000, 5000, 7000],
    buyer=['Иванов И.И.', 'Петров П.П.', 'Силоров С.С.'],
    date=['20.01.2023', '21.01.2023', '02.02.2023'])
