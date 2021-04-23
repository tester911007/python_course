import re
import requests

res = requests.get('https://stepik.org/media/attachments/lesson/245681/map2.osm').text
print(len(re.findall('fuel.*?</node>', res, flags=re.DOTALL)))

'''
Вася решил открыть АЗС (заправку). 
Чтобы оценить уровень конкуренции 
он хочет изучить количество заправок в интересующем его районе. 
Вася скачал интересующий его кусок карты OSM 
https://stepik.org/media/attachments/lesson/245681/map2.osm 
и хочет посчитать, сколько на нём отмечено точечных объектов (node), 
являющихся заправкой. 
В качестве ответа вам необходимо вывести одно число - количество АЗС.

"Как обозначается заправка в OpenStreetMap" - пример хорошего запроса чтобы узнать, 
как обозначается заправка в OpenStreetMap.
'''
