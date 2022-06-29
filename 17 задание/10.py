f = open("17 задание/10.txt")
nums = [int(x) for x in f.readlines()]

cnt = 0
mx_avg = 0
for i in range(len(nums) - 1):
    a = nums[i]
    b = nums[i+1]

    sm = a + b
    avg = sm / 2
    if sm % 2 == 0 and abs(sm) % 10 != 6:
        cnt += 1
        mx_avg = max(mx_avg, avg)

print(cnt, mx_avg)