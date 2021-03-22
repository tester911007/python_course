# Версия №1
import re
from collections import Counter

text = ''
with open('text.txt', 'r') as inf:
    for i in inf:
        text += i

regex = re.compile('\S{1,}')
count = Counter(matches.group() for matches in regex.finditer(text))

print(count)

# Версия №2
with open('text.txt') as f:
    text = f.read().lower().split()
popular_word = max(set(text), key=text.count)
print(popular_word, text.count(popular_word))
