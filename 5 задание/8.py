def f(N):
    n = bin(N)[2:]
    if N % 2 == 0:
        n = f"{n}{bin(n.count('1'))[2:]}"
    else:
        n = f"1{n}00"
    return int(n, 2)

for N in range(1, 10000):
    if f(N) > 215:
        print(N)
        break
