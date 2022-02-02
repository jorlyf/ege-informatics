from functools import lru_cache

def moves(s):
    return (s+1, s+3, s*2)

@lru_cache
def g(s):
    if s >= 26: return "w"
    
    if any( g(x) == "w" for x in moves(s) ): return "p1"
    if all( g(x) == "p1" for x in moves(s) ): return "v1"
    if any( g(x) == "v1" for x in moves(s) ): return "p2"
    if all( (g(x) == "p2" or g(x) == "p1") for x in moves(s) ): return "v2"

print(".19")
for s in range(1, 26):
    if g(s) == "v1": print(s); break

print(".20")
for s in range(1, 26):
    if g(s) == "p2": print(s)

print(".21")
for s in range(1, 26):
    if g(s) == "v2": print(s); break