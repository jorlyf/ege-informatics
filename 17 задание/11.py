f = open("17 задание/11.txt")
nums = [int(x) for x in f.readlines()]

mx3 = max(nums) * 3

cnt = 0
mxAvgGeom = 0
mnAvgGeom = 1000000000
for i in range(len(nums) - 1):
    a = nums[i]; b = nums[i+1]

    avgGeom = (a*b)**0.5

    if int(avgGeom)**2 == a*b or (int(avgGeom)+1)**2 == a*b:     
        if avgGeom <= mx3 and (a <= mx3 or b <= mx3):
            cnt += 1
            mxAvgGeom = max(mxAvgGeom, avgGeom)
            mnAvgGeom = min(mnAvgGeom, avgGeom)


print(cnt, mxAvgGeom + mnAvgGeom)