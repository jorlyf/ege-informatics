"""
На вход программе подается последовательность символов, которая заканчивается значком #
Размер файла не превышает 10^6 символов.
Программа должна вывести на экран символ, встречающийся чаще всего и его кол-во.

ABCD #
ABCE #
ABCF #
ответ: ABC 3

Day, mice. "Year" - a mistake #
ответ: A 4
"""

"""
A: P 33
B: CJX 22121
"""

f = open("27 задание/8b.txt")

symbols = dict()
s = f.readline()
for j in s:
    if j == " ": continue

    if not symbols.get(j.capitalize()):
        symbols[j.capitalize()] = 0
    symbols[j.capitalize()] += 1

print(symbols)

