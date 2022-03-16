s = "1" * 61
while "111" in s or "666" in s:
    if "111" in s:
        s = s.replace("111", "6", 1)
    else:
        s = s.replace("666", "1", 1)

print(s)