f = open("17 задание/13.txt")
nums = [int(x) for x in f.readlines()]

cnt = 0
mx = 0
for i in range(len(nums) - 1):
    a = nums[i]; b = nums[i+1]

    if abs(a) % 3 == 0 or abs(b) % 3 == 0:
        cnt += 1
        mx = max(mx, a+b)

print(cnt, mx)