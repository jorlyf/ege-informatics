f = open("17 задание/14.txt")
nums = [int(x) for x in f.readlines()]

cnt = 0
mnSm = 100000

mn37 = min([x for x in nums if x % 37 == 0])
mx73 = max([x for x in nums if x % 73 == 0])

print(mn37, mx73)

for i in range(len(nums)-1):
    a = nums[i]; b = nums[i+1]

    if ((mx73 < a < mn37) and (not (mx73 < b < mn37))) or ((not (mx73 < a < mn37)) and (mx73 < b < mn37)):
        cnt += 1
        mnSm = min(mnSm, a + b)

print(cnt, mnSm)