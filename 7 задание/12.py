x, y = 192, 960
colors = 2048
i = 11

V = x * y * i
Vkb = V / 2 ** 13
print(Vkb)

print(180 * 100 / Vkb)