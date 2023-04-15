"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet
import os

ARGS = ['ping', 'youtube.com']
ya_ping = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
print(ya_ping.stdout)
for i in ya_ping.stdout:
    res = chardet.detect(i)
    print(res)
    print(i.decode(encoding=res['encoding']))

ARGS = ['ping', 'yandex.ru']
ya_ping = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
print(ya_ping.stdout)
for i in ya_ping.stdout:
    res = chardet.detect(i)
    print(res)
    print(i.decode(encoding=res['encoding']))

print(os.name)
