f = open("27 задание/13b.txt")
N = int(f.readline())

k62 = 0
k31 = 0
k2 = 0
kOther = 0

for _ in range(N):
    x = int(f.readline())

    if x % 62 == 0:
        k62 += 1
    elif x % 31 == 0:
        k31 += 1
    elif x % 2 == 0:
        k2 += 1
    else:
        kOther += 1

print(k62, k31, k2, kOther)

q = k62 * (k62-1) // 2
q += k62 * k31
q += k62 * k2
q += k31 * k2
q += k62 * kOther

print(q)