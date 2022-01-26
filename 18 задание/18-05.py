import itertools

f = open("18 задание/18-05.txt")
nums = []
for s in f.readlines():
    nums.append(int(s))

b2 = list(itertools.permutations(nums, 2)) # все варианты подарков по 2

count1 = 0
count2 = 0

for b in b2:
    if (sum(b) <= 5000) and (b[0] != b[1]):
        count1 += 1
    if (sum(b) <= 15000) and (b[0] != b[1]):
        count2 += 1

print(count1 // 2, count2 // 2)