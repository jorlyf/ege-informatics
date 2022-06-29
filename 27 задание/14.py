f = open("27 задание/14b.txt")
N = int(f.readline())

a = dict()

for _ in range(N):
    x = int(f.readline())
    a[x] = 1

for i in range(N+1):
    x = a.get(i)
    if x == None:
        print(i)