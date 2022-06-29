def f(n):
    s1 = int(str(n)[0]) + int(str(n)[1])
    s2 = int(str(n)[1]) + int(str(n)[2])
    q = [s1, s2]
    q.sort()
    q.reverse()

    return f"{q[0]}{q[1]}"

for n in range(100, 1000):
    if f(n) == "156":
        print(n)