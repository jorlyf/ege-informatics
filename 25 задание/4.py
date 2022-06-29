простые_числа = {2}

for x in range(3, 100, 2):
    простое = True
    for j in простые_числа:
        if x % j == 0:
            простое = False
            break
    if простое: простые_числа.add(x)

print(простые_числа)

max_len = 0
отрезки = []
текущий_отрезок = []
for x in range(15_000_000, 16_000_000+1):
    сумма_цифр = sum(list(map(int, str(x))))
    if сумма_цифр not in простые_числа:
        текущий_отрезок.append(x)
        if max_len < len(текущий_отрезок):
            max_len = len(текущий_отрезок)
            отрезки.clear()
    else:
        отрезки.append(текущий_отрезок)
        текущий_отрезок = []

for q in отрезки:
    if len(q) == max_len:
        print(q)