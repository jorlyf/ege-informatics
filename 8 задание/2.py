# Сколько существует чисел, делящихся на 5, десятичная запись которых содержит 6 цифр,
# причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.


cnt = 0
for num in range(100_000, 1_000_000):
    if num % 5 != 0: continue

    if any(str(num).count(x) > 1 for x in "0123456789"): continue

    if any(f"{x}{y}" in str(num) for x in "13579" for y in "13579"):
        continue
    if any(f"{x}{y}" in str(num) for x in "24680" for y in "24680"):
        continue

    cnt += 1

print(cnt)