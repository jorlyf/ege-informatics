# Автомат получает на вход четырёхзначное число (число не может начинаться с нуля).
# По этому числу строится новое число по следующим правилам.
# 1. Складываются отдельно первая и вторая, вторая и третья, третья и четвёртая цифры заданного числа.
# 2. Наименьшая из полученных трёх сумм удаляется.
# 3. Оставшиеся две суммы записываются друг за другом в порядке неубывания без разделителей.
# Пример. Исходное число: 1982. Суммы: 1 + 9 = 10, 9 + 8 = 17, 8 + 2 = 10. Удаляется 10. Результат: 1017.
# Укажите наибольшее число, при обработке которого автомат выдаёт результат 1315.
# Примечание. Если меньшие из сумм равны, то отбрасывают одну из них.

def p(x):
    xstr = str(x)
    sums = []
    sums.append(int(xstr[0]) + int(xstr[1]))
    sums.append(int(xstr[1]) + int(xstr[2]))
    sums.append(int(xstr[2]) + int(xstr[3]))
    sums.remove(min(sums))
    sums.sort()
    sums = map(str, sums)
    return "".join(sums)

for x in range(1000, 10000):
    if p(x) == "1315":
        print(x)
