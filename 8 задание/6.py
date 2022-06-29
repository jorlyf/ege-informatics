nums = [x for x in range(10000, 100_000)]

cnt = 0
for num in nums:
    snum = str(num)

    if snum[-1] in "347":
        continue

    if "000" in snum or "111" in snum or "222" in snum or "333" in snum or "444" in snum or\
        "555" in snum or "666" in snum or "777" in snum or "888" in snum or "999" in snum:
        print(snum)
        continue

    cnt += 1

print(cnt)