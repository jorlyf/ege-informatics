f = open("27 задание/olymp2B.txt")
N = int(f.readline())

a = []
for i in range(N):
    a.append(int(f.readline()))

zero_array = []
cnt = 0

for k in range(N):
    if a[k] == 0:
        zero_array.append(k)

for i in range(N):
    x = a[i]

    for j in range(i+1, N):
        y = a[j]
    
        сумма = x + y
        if x == 0 or y == 0: continue
        if сумма % 2 != 0: continue
        
        for q in zero_array:
            if i < q < j:
                cnt += 1
                break
    
    if i % 1_000 == 0: print(i)

print(cnt)