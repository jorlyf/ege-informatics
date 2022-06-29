f = open("27 задание/19b.txt")

a = f.readline()
d = dict()
for s in a:
    s = s.capitalize()
    if not d.get(s):
        d[s] = 0
    d[s] += 1


alphabet = sorted("ABCDEFGHIKLMNOPQRSTVXYZJUW")
alphabet.reverse()

answer = ""

print(d)

for i in range(26):
    let = ""
    mn = 100000
    for letter in alphabet:
        if not d.get(letter): continue
        mn = min(mn, d[letter])
        if d[letter] == mn:
            let = letter
    if let != "":
        answer += let
        d.pop(let)

print(answer)