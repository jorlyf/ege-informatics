import itertools

a = list(itertools.product("ДЕЙНПТЬЯ", repeat=4))

i = 0
for word in a:
    word = "".join(word)
    i += 1

    if "Я" not in word and "Е" not in word:
        if all( word.count(x) == 1 for x in word ):
            print(i, word)