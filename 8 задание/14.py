import itertools

a = set(itertools.permutations("СПОРТЛОТО", r=9))
b = set()
for word in a:
    word = "".join(word)
    if "О" != word[0]:
        b.add(word)

b = sorted(b)

print(len(b))
