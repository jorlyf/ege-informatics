s = "X" * 107
while "XXX" in s or "ZYX" in s or "ZXX" in s:
    s = s.replace("XXX", "ZZ", 1)
    s = s.replace("ZYX", "X", 1)
    s = s.replace("ZXX", "Y", 1)

print(s)