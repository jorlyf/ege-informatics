f = open("27 задание/olymp2A.txt")

N = int(f.readline())

a = []
for i in range(N):
    a.append(int(f.readline()))

zero_array = []
cnt = 0
print(a)
for k in range(N):
    if a[k] == 0:
        zero_array.append(k)

for i in range(N):
    x = a[i]

    for j in range(N):
        if i == j: continue
        y = a[j]
        #print(x, y)
    
        сумма = x + y
        if сумма % 2 != 0: continue
        
        for q in zero_array:
            if i < q < j:
                cnt += 1
                print(i, j)
    # if i % 10 == 0:
    #     print(i)

print(cnt)