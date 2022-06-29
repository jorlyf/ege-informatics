# 9c.txt = 29
# 9a.txt = 143124
# 9b.txt = 749251060

f = open("27 задание/9b.txt")
N = int(f.readline())

summa = 0
dmin = 1000000
for i in range(N):
    x = f.readline()
    a, b, c = map(int, x.split())
    summa += max(a, b, c)
    q = [a, b, c]
    q.sort()

    d = abs(q[2] - q[1])
    if d % 10 == 0: continue
    dmin = min(dmin, d)

print(dmin)
if summa % 10 != 0:
    print(summa)
else:
    print(summa-dmin)