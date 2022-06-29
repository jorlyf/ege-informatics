def f(N):
    n = bin(N)[2:]

    if N % 2 == 0:
        n = "1" + n + "0"
    else:
        n = "11" + n + "10"

    return int(n, 2)

mnR = 10000000000
for N in range(1, 100):
    R = f(N)
    sm = sum([int(x) for x in str(R)])
    if sm > 17:
        mnR = min(mnR, R)


sm = sum([int(x) for x in str(mnR)])
print(mnR)
print(bin(sm)[2:])

# R = f(14)
# print(R)