# Сколько существует чисел, делящихся на 5, десятичная запись которых содержит 6 цифр,
# причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
import itertools

a = list(itertools.product("0123456789", repeat=6))
nums = []
for s in a:
    s = "".join(s)
    if s[0] != "0" and int(s) % 5 == 0:
        if all(s.count(x) <= 1 for x in "0123456789"):
            последнийЧетный = False
            flag = True
            for i in range(0, len(s)):
                if int(s[i]) % 2 == 0:
                    if последнийЧетный:
                        flag = False
                        break
                    последнийЧетный = True
                else:
                    if not последнийЧетный:
                        flag = False
                        break
                    последнийЧетный = False
            
            if flag:
                nums.append(s)

print(len(nums))