from functools import lru_cache

def moves(s):
    a = s[0]; b = s[1]
    return (a+1, b), (a*2, b), (a, b+1), (a, b*2)

@lru_cache(None)
def g(s):
    if sum(s) >= 73: return "W"

    if any(g(x) == "W" for x in moves(s)): return "P1"
    if all(g(x) == "P1" for x in moves(s)): return "V1"
    if any(g(x) == "V1" for x in moves(s)): return "P2"
    if all(g(x) == "P2" or g(x) == "P1" for x in moves(s)): return "V2"

print("/19")
for s in range(1, 63+1):
    if g((9, s)) == "V1":
        print(s) # 16
        break

print("/20")
for s in range(1, 63+1):
    if g((9, s)) == "P2":
        print(s) # 27 31

print("/21")
for s in range(1, 63+1):
    if g((9, s)) == "V2":
        print(s) # 26