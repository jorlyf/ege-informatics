x = 500_000

while True:
    делители = set()
    for q in range(1, int(x**1/2) + 5):
        if x % q == 0:
            делители.add(q)
            делители.add(x//q)
    делители = sorted(делители)
    for q in делители:
        if str(q)[-1] == "8" and q != 8 and q != x:
            print(x, q)
            break
    x += 1