def получить_делители(x: int):
    s = set()
    for i in range(2, int(x**1/2) + 5):
        if x % i == 0:
            if i % 2 == 0: continue
            s.add(i)
            if (x//i) % 2 == 0: continue
            s.add(x // i)

    return list(s)

def D(s: list):
    if len(s) < 6: return 0
    s.sort()
    s.reverse()
    return s[5]

x = 200_000_001
cnt = 0
while True:
    делители = получить_делители(x)
    if D(делители) > 0:
        cnt += 1
        print(x, D(делители))
        if cnt == 10:
            break
    x += 1
