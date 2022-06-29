f = open("27 задание/12b.txt")
N = int(f.readline())

k14 = 0
k7 = 0
k2 = 0
kOther = 0

for i in range(N):
    x = int(f.readline())

    if x % 14 == 0:
        k14 = max(k14, x)
    if x % 7 == 0:
        k7 = max(k7, x)
    if x % 2 == 0:
        k2 = max(k2, x)

    kOther = max(kOther, x)

X = max(
    k14 * kOther,
    k7*k2
)

print(X)