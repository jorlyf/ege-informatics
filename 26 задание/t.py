f = open("26 задание/t.txt")
nums = list(map(int, f.readlines()))
dd = dict()
for i in nums:
    if dd.get(i):
        dd[i] += 1
    else:
        dd[i] = 1

mx = 0
q = 1
for zarplata in dd:
    if dd[zarplata] > mx:
        mx = dd[zarplata]
        q = zarplata

print(q)

