print("x y z w")
ans = []
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x <= y) and (y <= z) and (z <= w):
                    ans.append([str(x), str(y), str(z), str(w)])

ans.pop(0)
ans.pop(3)
for a in ans:
    print(" ".join(a))