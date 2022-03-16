# Алгоритм вычисления функции F(n) задан следующими соотношениями:
# F(n) = n, при n ≤ 5,
# F(n) = n + F(n / 3 + 2), когда n > 5 и делится на 3,
# F(n) = n + F(n + 3) , когда n > 5 и не делится на 3.
# Определите минимальное значение n, для которого вычисления закончатся и значение F(n) > 1000.

def F(n):
    if n <= 5: return n
    if n % 3 == 0: return n + F(n//3 + 2)
    return n + F(n+3)

for n in range(1, 1000):
    try:
        if F(n) > 1000: print(n, F(n))
    except RecursionError:
        pass