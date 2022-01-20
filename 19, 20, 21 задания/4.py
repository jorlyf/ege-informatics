"""
+1, +3, *2
win >= 24
1 <= S <= 23
"""

from functools import lru_cache

def moves(x):
    return (x+1, x+3, x*2)

@lru_cache(None)
def g(s):
    if s >= 24: return "w"
    if any( g(x) == "w" for x in moves(s) ): return "p1"
    if all( g(x) == "p1" for x in moves(s) ): return "v1" # заменить на any для первой задачи
    if any( g(x) == "v1" for x in moves(s) ): return "p2"
    if all( g(x) in ("p1", "p2") for x in moves(s) ): return "v2"


for s in range(1, 23+1):
    print(s, g(s))


print("Задание 19")
for s in range(1, 23+1):
    if g(s) == "v1": print(s); break

print("Задание 20")
for s in range(1, 23+1):
    if g(s) == "p2": print(s)

print("Задание 21")
for s in range(1, 23+1):
    if g(s) == "v2": print(s); break