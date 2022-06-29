def f(N):
    n = bin(N)[2:]

    if n.count("1") > n.count("0"):
        n = n + "0"
    else:
        n = "11" + n

    if n.count("1") > n.count("0"):
        n = n + "0"
    else:
        n = "11" + n
    
    return int(n, 2)

for N in range(1, 1000):
    if f(N) > 500:
        print(N)
        break