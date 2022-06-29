# 11c.txt => 140 100
# 11a.txt => 8096 6544

m = 120

f = open("27 задание/11c.txt")
N = int(f.readline())

k = [0] * m

left = 0
right = 0

for i in range(N):
    x = int(f.readline())

    остаток = x % m
    if остаток == 0:
        if k[0] > x and k[0] + x > left + right:
            left = k[0]
            right = x
    else:
        if k[m-остаток] > x and k[m-остаток] + x > left + right:
            left = k[m-остаток]
            right = x
    
    if x > k[остаток]:
        k[остаток] = x

print(left, right)