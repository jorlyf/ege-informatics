def F(n):
    if n > 25:
        return n*n + 4*n + 3
    if n % 3 == 0:
        return F(n+1) + 2*F(n+4)
    return F(n+2) + 3*F(n+5)

count = 0
for n in range(1, 1000+1):
    f = str(F(n))
    сумма_цифр = sum(map(int, f))
    if сумма_цифр == 24: count +=1
    
print(count)