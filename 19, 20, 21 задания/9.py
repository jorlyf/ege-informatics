from functools import lru_cache

def moves(s):
    a = s[0]
    b = s[1]
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2)

@lru_cache(None)
def g(s):
    if sum(s) >= 53: return "W"

    if any( g(x) == "W" for x in moves(s) ): return "P1"
    if all( g(x) == "P1" for x in moves(s) ): return "B1"
    if any( g(x) == "B1" for x in moves(s) ): return "P2"
    if all( g(x) == "P1" or g(x) == "P2" for x in moves(s) ): return "B2"
    
for s in range(1, 43+1):
    if g((9, s)) == "B2":
        print(s)




