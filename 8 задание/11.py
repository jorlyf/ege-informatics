import itertools

a = list(itertools.product("АИКЛМЬ", repeat=6))


words = []

i = 0
for word in a:
    word = "".join(word)
    i += 1

    words.append( (i, word) )


i = 0
for word in a:
    word = "".join(word)
    i += 1

    if word[0] == "К" and word[-1] == "Ь":
        if all( word.count(x) == 1 for x in "АИКЛМЬ" ):
            #print(i, word)
            
            # for p in words:
            #     ind = p[0]
            #     wordp = p[1]

            #     if word == wordp[::-1]:
            #         if abs(i - ind) == 26655:
            #             print(i)

            if i > 26655:
                if word == words[i - 26655 - 1][1][::-1]:
                    print(i, word, words[i - 26655])
            elif len(words) > i + 26655:
                if word == words[i + 26655 - 1][1][::-1]:
                    print(i, word, words[i + 26655])
