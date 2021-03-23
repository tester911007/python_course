'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''

import requests

file_contents = '699991.txt'
url = 'https://stepic.org/media/attachments/course67/3.6.3/'

while file_contents[:3] != 'We ':
    file_contents = requests.get(url + file_contents).text
print(file_contents)

