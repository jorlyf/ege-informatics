import itertools

a = list(itertools.product("МЕТРО", repeat=4))
cnt = 0

for w in a:
    w = "".join(w)
    if w[0] in "МТР" and w[3] in "ЕО":
        cnt += 1
        print(w)

print(cnt)