f = open("17 задание/9.txt")
nums = [int(x) for x in f.readlines()]

mxKR11 = max([x for x in nums if x % 11 == 0]) # 990

cnt = 0
mx_sm = 0
for i in range(len(nums)-1):
    a = nums[i]
    b = nums[i+1]

    if a % 11 == 0 or b % 11 == 0:
        sm = a + b
        if sm <= mxKR11:
            cnt += 1
            mx_sm = max(mx_sm, sm)

print(cnt, mx_sm)