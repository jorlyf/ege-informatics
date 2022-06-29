s = []
cnt = 0
mx = 0
mn = 10000
mx_len = 0
for x in range(1079, 9895+1):
    if x % 14 == 0 and x % 10 != 2 and x % 10 != 6 and x % 5 != 0 and x % 28 != 0:
        mx = max(mx, x)
        if cnt > mx_len:
            mx_len = cnt
            print(mx_len, x)
        cnt = 0
    else:
        cnt += 1
print(mx)

z = [x for x in range(1079, 9895+1) if x % 14 == 0 and x % 10 != 2 and x % 10 != 6 and x % 5 != 0 and x % 28 != 0 ]
q = [x for x in range(1079, 9895+1)]
print(z)
print(q[1125:1220])
