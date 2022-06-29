f = open("27 задание/18b.txt")
N = int(f.readline())

a = [int(f.readline()) for _ in range(N)]

cnt = 0
for i in range(0, N):
    for j in range(i+1, N):
        x = a[i]
        y = a[j]

        if abs(x - y) % 13 != 0: continue
        if x*y % 2 != 0: continue

        cnt += 1

    if i % 100 == 0:
        print(i)
        
print(cnt)