# (z or not (y)) and (z or x)

print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (z or not (y)) and (z or x):
                print(x, y, z)
