a = [x for x in range(1404, 9522+1) if x % 7 != 0 and x % 9 != 0 and x % 19 != 0 and x % 10 == 3]

mx_len = 0
for i in range(len(a)-1):
    mx_len = max(a[i+1] - a[i], mx_len)

print(a[-200], mx_len - 1)