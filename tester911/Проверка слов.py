'''
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках указываются эти слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:

stepic
champignons
the
'''

d = int(input())

words = []
for i in range(d):
    words.append(input().lower())

l = int(input())
text = []
for i in range(l):
    text.append(input().lower().split())

unique_words = []
for i in text:
    for j in i:
        check = False
        for word in words:
            if word == j:
                check = True

        if not check:
            unique_words.append(j)
        check = False

for i in set(unique_words):
    print(i)
