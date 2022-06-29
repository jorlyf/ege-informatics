import itertools

words = list(itertools.product("ВЕКНО", repeat=5))

i = 0
for word in words:
    word = "".join(word)
    i += 1

    if word.count("Н") == 2 and word.count("К") == 2:
        print(i, word)