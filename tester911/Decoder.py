'''
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то странным набором звуков.

В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:

abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:

*d*%*d*#*d*
dacabac
Sample Input 2:

dcba
badc
dcba
badc
Sample Output 2:

badc
dcba
'''

# Версия 1
text = input()
code = input()

message_1 = input()
message_2 = input()


def coder(message, decoder=False):
    result = []
    for j in message:
        result.append(j)
        for i in range(len(text)):
            buffer = result[-1]
            if decoder:
                result[-1] = result[-1].replace(code[i], text[i])
            else:
                result[-1] = result[-1].replace(text[i], code[i])

            if buffer != result[-1]:
                break

    return result


answer = coder(message_1, decoder=False)
print(*answer, sep='')
answer = coder(message_2, decoder=True)
print(*answer, sep='')

# Версия 2
a, b, c, d = input(), input(), input(), input()
print(''.join(b[a.index(i)] for i in c))
print(''.join(a[b.index(i)] for i in d))

# Версия 3
source, dest = input(), input()
decoded = input()
encoded = input()

print(decoded.translate(str.maketrans(source, dest)))
print(encoded.translate(str.maketrans(dest, source)))
