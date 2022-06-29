import itertools

a = list(itertools.product(sorted("ЛЕТО"), repeat=4))

cnt = 0
for x in a:
    x = "".join(x)

    if x[0] in "ЛТ":
        cnt += 1

print(cnt)
    