f = open("24 задание/4.txt")
s = f.readline()
цифры = "0123456789"
mnNum = 100000000000

текущее_число = ""
for i in range(0, len(s)):
    if s[i] in цифры:
        текущее_число += s[i]
    else:
        if текущее_число != "" and int(текущее_число) > 999 and int(текущее_число) < 100_000_000:
            mnNum = min(int(текущее_число), mnNum)
        текущее_число = ""

print(mnNum)