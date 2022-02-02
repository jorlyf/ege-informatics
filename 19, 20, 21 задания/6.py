"""
+2
+3
*2

win >= 40
"""
from functools import lru_cache


winS = 40 
def moves(s):
    return (s+2, s+3, s*2)

@lru_cache
def g(s):
    if s >= winS: return "w"

    if any( g(x) == "w" for x in moves(s) ): return "p1"
    if all( g(x) == "p1" for x in moves(s) ): return "v1" # заменить на any для 19 задания
    if any( g(x) == "v1" for x in moves(s) ): return "p2"
    if all( g(x) in ["p1", "p2"] for x in moves(s) ): return "v2"

print("19 zadanie")
for s in range(1, 39):
    if g(s) == "v1":
        print(s)
        break

print("20 zadanie")
for s in range(1, 39):
    if g(s) == "p2":
        print(s)
        break

print("21 zadanie")
for s in range(1, 39):
    if g(s) == "v2":
        print(s)
        break


