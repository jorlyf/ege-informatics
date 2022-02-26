f = open("26 задание/2.txt")

vexels = list(map(int, f.readlines()))[1:] # все вексели
vexels.sort()

mn = 10000000000
a = 0
for i in range(1, len(vexels)):
    if sum(vexels[:i]) < vexels[i]:
        mn = sum(vexels[:i])
        a = len(vexels[:i])
        print(mn+1, a, i)

