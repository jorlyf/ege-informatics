def f(N):
    n = bin(N)[2:]
    ni = ""
    for q in n:
        if q == "1": q = "0"
        else: q = "1"
        ni += q
    ni = int(ni, 2)
    return N - ni

for N in range(1, 1000):
    R = f(N)
    if R > 37:
        print(N)
        break