import itertools

q = "А Б Г О Щ".split()
q.reverse()
qw = "".join(q)

words = list(itertools.product(qw, repeat=6))
index = 0
for word in words:
    index += 1
    word = "".join(word)
    if word == "ОБЩАГА":
        print(index)