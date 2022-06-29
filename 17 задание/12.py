f = open("17 задание/12.txt")
nums = [int(x) for x in f.readlines()]

mn103 = min([x for x in nums if x % 103 == 0])
print(mn103)

cnt = 0
mxs = 0
for i in range(len(nums) - 1):
    a = nums[i]; b = nums[i+1]

    if ((a + b) % 2 == 0) and (abs(a - b) % mn103 == 0):
        cnt += 1
        mxs = max(mxs, a+b)
        print(a, b, a+b)
    
print(cnt, mxs)