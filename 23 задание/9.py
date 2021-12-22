"""
У исполнителя есть три команды, которым присвоены номера:
1. Прибавь 1
2. Умножь на 2
3. Сделай нечётное
Первая команда увеличивает число на 1, вторая – вдвое,
третья прибавляет к четному числу 1, к нечетному – 2.
Сколько существует таких программ,
которые исходное число 3 преобразуют в число 25
и при этом траектория вычислений содержит число 9 и число 17?
"""
def f(x, end):
    if x > end: return 0
    if x == end: return 1
    a = f(x+1, end)
    b = f(x*2, end)
    if x % 2 == 0: c = f(x+1, end)
    else: c = f(x+2, end)

    return a+b+c

print( f(3, 9) * f(9, 17) * f(17, 25) )