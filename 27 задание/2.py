"""
Найти минимальное произведение двух элементов последовательности
8
3
4
5
-7
-8
2
3
9
"""

f = open("27 задание/2b.txt")
N = int(f.readline())

mn_less_0 = 0
mx_bigger_0 = 0

только_положительные = False
только_отрицательные = False

for _ in range(N):
    x = int(f.readline())
    mn_less_0 = min(mn_less_0, x)
    mx_bigger_0 = max(mx_bigger_0, x)

print(mn_less_0 * mx_bigger_0)