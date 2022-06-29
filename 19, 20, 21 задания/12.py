from functools import lru_cache


def moves(h):
    return (h+2), (h+3), (h*2)

@lru_cache(None)
def g(h):
    if h >= 30: return "W"

    if any(g(s) == "W" for s in moves(h)):
        return "P1"
    if all(g(s) == "P1" for s in moves(h)):
        return "V1"
    if any(g(s) == "V1" for s in moves(h)):
        return "P2"
    if all(g(s) == "P1" or g(s) == "P2" for s in moves(h)):
        return "V1/V2"

print("19 задание")
for s in range(1, 29+1):
    if g(s) == "V1":
        print(s)
        break

print("20 задание")
for s in range(1, 29+1):
    if g(s) == "P2":
        print(s)

print("21 задание")
for s in range(1, 29+1):
    if g(s) == "V1/V2":
        print(s)