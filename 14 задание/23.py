a = 5**94 + 25**49 - 130
cnt = 0
num = ""
while a > 0:
    if a % 5 == 4: cnt += 1
    num = str(a % 5) + num
    a = a // 5

print(num.count("4"))
print(cnt)