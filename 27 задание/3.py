"""
Найти максимальное произведение, кратное 6, из двух разных элементов
"""
f = open("27 задание/3b.txt")
N = int(f.readline())

k1 = []
k2 = []
k3 = []
k6 = []

for _ in range(N):
    x = int(f.readline())
    if x % 6 == 0: k6.append(x)
    elif x % 3 == 0: k3.append(x)
    elif x % 2 == 0: k2.append(x)
    else: k1.append(x)

r = max([max(k1)*max(k6), max(k2)*max(k3), max(k2)*max(k6), max(k3)*max(k6)])
print(r)