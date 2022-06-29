def f(N):
    n = bin(N)[2:]
    if N % 2 == 0:
        R = "1" + n + "00"
    else:
        R = "10" + n + "1"

    return int(R, 2)

N = 1
while True:
    if f(N) < 1000:
        print(N, f(N))
        
    N += 1