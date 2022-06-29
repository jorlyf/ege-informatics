"""
Найти количество пар, для которых
произведение элементов делится на 6 и при этом
номера элеменов пары различаются не менее, чем на 4
"""

f = open("27 задание/16a.txt")
N = int(f.readline())

буффер = [int(f.readline()) for _ in range(4)]

k = 0
k2 = 0
k3 = 0
k6 = 0

r = 0


for _ in range(N-4):
    if буффер[0] % 2 == 0: k2 += 1
    if буффер[0] % 3 == 0: k3 += 1
    if буффер[0] % 6 == 0: k6 += 1
    k += 1

    x = int(f.readline())

    if x % 6 == 0:
        r += k
    elif x % 3 == 0:
        r += k2
    elif x % 2 == 0:
        r += k3
    else:
        r += k6

    буффер.append(x)
    буффер.pop(0)

print(r)

f.close()