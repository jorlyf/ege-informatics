f = open("17 задание/6.txt")
s = f.readlines()

a = []
for k in s:
    a.append(int(k))

ср_арифм = sum(a) / len(a)

cnt = 0
mx_sum = 0
for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]

    if x > ср_арифм or y > ср_арифм: continue
    if x % 10 != 9 and y % 10 != 9: continue
    cnt += 1
    mx_sum = max(mx_sum, x+y)

print(cnt, mx_sum)
