# Автомат получает на вход два трехзначных числа.
# По этим числам строится новое число по следующим правилам.
# Вычисляются три числа – сумма старших разрядов заданных трехзначных чисел,
# сумма средних разрядов этих чисел, сумма младших разрядов.
# Полученные три числа записываются друг за другом в порядке неубывания (без разделителей).
# Пример. Исходные трехзначные числа:  835, 196. Поразрядные суммы: 9, 12, 11. Результат: 91112
# Какое наибольшее значение может иметь одно из чисел, полученных на входе,
# если другое число равно 365, а в результате работы автомата получено число 51014?

def f(A, B):
    Astr = str(A)
    Bstr = str(B)
    сумма_старших_разрядов = int(Astr[0]) + int(Bstr[0])
    сумма_средних_разрядов = int(Astr[1]) + int(Bstr[1])
    сумма_младших_разрядов = int(Astr[2]) + int(Bstr[2])
    c = [сумма_старших_разрядов, сумма_средних_разрядов, сумма_младших_разрядов]
    c.sort()

    return str(c[0]) + str(c[1]) + str(c[2])

for x in range(100, 1000):
    y = 365
    if f(x, y) == "51014":
        print(x)