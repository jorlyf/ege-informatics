f = open("24 задание/7.txt")
a = f.readline()

max_cnt = 0
cnt = 0

s = ""
max_s = ""
for x in a:
    s += x

    if "XY" in s or "XZ" in s:       
        if cnt > max_cnt:
            max_s = s[:-1]
        max_cnt = max(max_cnt, cnt+1)
 
        cnt = 0
        s = x
    else:
       cnt += 1

print(max_cnt)
print(max_s, len(max_s))