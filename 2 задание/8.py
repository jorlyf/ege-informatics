print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (y and (not z)) or ((not x) and (not z))
            if f:
                print(x, y, z)