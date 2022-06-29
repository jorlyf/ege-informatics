import itertools

a = list(itertools.product("0123456", repeat=7))
count = 0
for num in a:
    num = "".join(num)
    num = int(num)
    if len(str(num)) < 7: continue

    if str(num)[0] in "35": continue
    if "22" in str(num) and "44" in str(num): continue

    count += 1

print(count)