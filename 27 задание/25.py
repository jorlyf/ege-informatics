f = open("27 задание/25a.txt")
N = int(f.readline())
nums = [0]*N
for i in range(N):
    nums[i] = int(f.readline())


q = []

mx_sm = 0
ln = 1000000
for i in range(0, N):
    sm = 0
    for j in range(i, N):
        sm += nums[j]

        if sm % 89 == 0:
            if sm > mx_sm:
                q.clear()
            if sm >= mx_sm:
                mx_sm = sm
                ln = j - i + 1
                q.append((mx_sm, ln))
        
print(q)