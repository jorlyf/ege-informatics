print("a b c f")
for a in range(2):
    for b in range(2):
        for c in range(2):
            f = int((a and b) or (a and (not c)))
            print(a, b, c, f)