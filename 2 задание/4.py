# (z and x) or ((-x) and -y) == true

print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (z and x) or ((not x) and not y):
                print(x, y, z)