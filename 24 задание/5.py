f = open("24 задание/5.txt")
s = f.readline()
f.close()

min_cnt = 10000000
cnt = 0
for i in range(len(s)):
    x = s[i]
    if x in "ABC": cnt += 1
    else:
        min_cnt = min(min_cnt, cnt)
        cnt = 0

print(min_cnt)