from functools import lru_cache

def moves(h):
    return (h+1), (h+2), (h*2)

@lru_cache
def g(h):
    if h >= 22: return "W"

    if any(g(s) == "W" for s in moves(h)): return "P1"
    if all(g(s) == "P1" for s in moves(h)): return "V1"
    if any(g(s) == "V1" for s in moves(h)): return "P2"
    if all(g(s) == "P2" or g(s) == "P1" for s in moves(h)): return "V1/V2"

print("ex.19")
for s in range(1, 22):
    if g(s) == "V1":
        print(s)

print("ex.20")
for s in range(1, 22):
    if g(s) == "P2":
        print(s)

print("ex.21")
for s in range(1, 22):
    if g(s) == "V1/V2":
        print(s)