a = 5**2004 - 5**1016 - 25**508 - 5**400 + 25**250 - 27
cnt = 0
while a > 0:
    #s += str(a % 5) + s 
    if (a % 5 == 4):
        cnt += 1 
    a = a // 5

print(cnt)