print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = ((not x) <= y) and ((not y) == z) and w
                if F:
                    print(w, x, y, z)