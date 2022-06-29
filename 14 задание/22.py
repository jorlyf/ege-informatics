a = (7**(9**2 - 1) - (10-3)**4 + int("234", 7)) * 5/6 * 8
print(a)
cnt = 0
while a > 0:
    if a % 7 == 4: cnt += 1
    a = a // 7
print(cnt)