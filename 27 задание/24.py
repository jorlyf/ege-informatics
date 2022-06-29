f = open("27 задание/24a.txt")

nums = [int(x) for x in f.readlines()]

mx_sm = 0
for i in range(0, len(nums)):
    sm = 0
    for j in range(i, len(nums)):
        sm += nums[j]

        if sm % 67 == 0:
            mx_sm = max(mx_sm, sm)

print(mx_sm)