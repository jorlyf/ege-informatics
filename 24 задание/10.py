import string

f = open("24 задание/10.txt")

cnt = 0
for s in f.readlines():
    for q in string.ascii_uppercase:
        sub = f"Z{q}RO"
        if sub in s:
            cnt += 1
            break

print(cnt)