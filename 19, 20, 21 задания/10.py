from functools import lru_cache


def moves(s):
    return (s+2, s*3)

@lru_cache
def g(s):
    if s >= 50: return "W"

    if any(g(x) == "W" for x in moves(s)): return "P1"
    if all(g(x) == "P1" for x in moves(s)): return "V1"
    if any(g(x) == "V1" for x in moves(s)): return "P2"
    if all(g(x) == "P1" or g(x) == "P2" for x in moves(s)): return "V2"

# 1
for s in range(1, 49+1):
    if g(s) == "V1":
        print("1:", s)
        break

# 2
cnt = 0
for s in range(1, 49+1):
    if g(s) == "P2":
        cnt += 1
print("2:",cnt)

# 3
for s in range(1, 49+1):
    if g(s) == "P2":
        print("3:", s)