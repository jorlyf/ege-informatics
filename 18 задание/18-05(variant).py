f = open("18 задание/18-05.txt")
nums = list(map(int, f.readlines()))

import itertools
combinations = list(itertools.permutations(nums, r=2))

c5000 = 0
c15000 = 0
for x in combinations:
    if sum(x) <= 5000 and x[0] != x[1]: c5000 += 1
    if sum(x) <= 15000 and x[0] != x[1]: c15000 += 1

print(c5000/2, c15000/2)