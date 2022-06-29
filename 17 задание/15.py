f = open("17 задание/15.txt")
nums = [int(x) for x in f.readlines()]

cnt = 0
mnsm = 100000000

kr111 = max([x for x in nums if x % 111 == 0])

for i in range(len(nums) - 1):
    a = nums[i]; b = nums[i+1]

    if a > kr111 or b > kr111:
        if a % 10 == 7 or b % 10 == 7:
            cnt += 1
            mnsm = min(mnsm, a + b)

print(cnt, mnsm)