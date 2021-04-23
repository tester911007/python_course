import glob
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

import xlrd

zip_url = 'https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip'
path = 'tmp/buffer'

with urlopen(zip_url) as zip_resp:
    with ZipFile(BytesIO(zip_resp.read())) as zip_file:
        zip_file.extractall(path)

file_names = glob.glob(path + '/*.xlsx')

fio_salary = dict()

for file_xlsx in file_names:
    wb = xlrd.open_workbook(file_xlsx)
    sheet = wb.sheet_by_index(0)
    fio_salary.update({sheet.cell_value(1, 1): int(sheet.cell_value(1, 3))})

with open(path + '/tmp.txt', 'w', encoding='UTF-8') as ouf:
    for data in sorted(fio_salary.items()):
        ouf.write(f"{data[0]} {data[1]}\n")

'''
Главный бухгалтер компании "Рога и копыта" 
случайно удалил ведомость с начисленной зарплатой. 
К счастью, у него сохранились расчётные листки всех сотрудников. 
Помогите по этим расчётным листкам восстановить зарплатную ведомость. 
Архив с расчётными листками доступен по ссылке 
https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip 
(вы можете скачать и распаковать его вручную 
или самостоятельно научиться делать это с помощью скрипта на Питоне).

Ведомость должна содержать 1000 строк, 
в каждой строке должно быть указано ФИО сотрудника и, 
через пробел, его зарплата. Сотрудники должны быть упорядочены по алфавиту.
'''
