f = open("17 задание/39762.txt")

nums = list(map(int, f))

count = 0
mx = 0
for i in range(0, len(nums) - 2):
    x1 = nums[i]
    x2 = nums[i+1]

    if (x1*x2) % 15 == 0:
        if (x1+x2) % 7 == 0:
            count += 1
            mx = max(mx, x1+x2)

print(count, mx)