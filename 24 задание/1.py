f = open("24 задание/24-05.txt")
a = f.readline()


count = 0
nums = []
ts = ""
for i in range(1, len(a)):
    if a[i] in "0123456789":
        count += 1
        ts += str(a[i])
        if count == 3 and a[i+1] not in "0123456789":
            nums.append(ts)
            ts = ""
    else: count = 0; ts = ""

a = list(map(int, nums))
print(sum(a))
    