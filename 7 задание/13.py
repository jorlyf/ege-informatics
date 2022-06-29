x, y = 128, 320
V = 20 * 2**13

i = int(V / x / y)
print(2**i)