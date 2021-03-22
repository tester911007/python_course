import re

text = ''
with open('text.txt', 'r') as inf:
    for line in inf:
        a = re.findall("\w\d+", line)
        text += line
        for i in a:
            print(i)
            text = text.replace(i, i[0] * int(i[1:]))

with open('text.txt', 'w') as ouf:
    ouf.write(text)
