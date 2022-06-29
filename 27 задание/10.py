kостальные = 0
k2 = 0
k13 = 0
k26 = 0

f = open("27 задание/10b.txt")
N = int(f.readline())

for _ in range(N):
    x = int(f.readline())

    if x % 26 == 0:
        k26 += 1
    elif x % 13 == 0:
        k13 += 1
    elif x % 2 == 0:
        k2 += 1
    else:
        kостальные += 1
    
q = k26 * (k26-1) // 2
q += k26 * k13
q += k26 * k2
q += k26 * kостальные

q += k13 * k2

print(q)