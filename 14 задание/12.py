def changeBase(num, base):
    s = ""
    while num > 0:
        s = str(num % base) + s
        num = num // base
    return s

n = 1
while True:
    if changeBase(n, 4)[-1] == "0" and changeBase(n, 7)[-1] == "0":
        print(n, changeBase(n, 4), changeBase(n, 7))
        break

    n += 1