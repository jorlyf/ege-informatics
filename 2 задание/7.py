print("a b c f")
for a in range(2):
    for b in range(2):
        for c in range(2):
            f = (a and (not c)) or ((not b) and (not c))
            print(a, b, c, int(f))