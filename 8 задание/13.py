import itertools

a = list(itertools.product("ЕЛМРУ", repeat=4))

i = 0
for word in a:
    word = "".join(word)
    i += 1

    print(i, word)

    if word[0] == "Л":
        break
