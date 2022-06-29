print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (z or y) <= (x == z)
            if not f:
                print(x, y, z)