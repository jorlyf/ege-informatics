from re import A


a = 5**2004 - 5**1016 - 25**508 - 5**400 + 25**250 - 27
s = str(a)
while a > 0:
    s = str(a % 5) + s 
    a //= 5

print(s.count("4"))