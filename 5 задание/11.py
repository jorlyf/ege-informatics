def f(N):
    n = bin(N)[2:]

    n = n[1:]
    
    if n.count("1") % 2 == 0:
        n = "10" + n
    else:
        n = "1" + n + "0"

    return int(n, 2)

ans = 0
for N in range(1, 100000):
    R = f(N)
    if R < 450:
        ans = max(ans, R)

print(ans)
