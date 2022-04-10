f = open("24 задание/olymp1.txt")

a = f.readline()

def isPal(x):
    return x[0] == x[4] and x[1] == x[3]

cnt = 0
for i in range(4, len(a)):
    x = a[i-4] + a[i-3] + a[i-2] + a[i-1] + a[i]
    if isPal(x):
        cnt += 1

print(cnt)