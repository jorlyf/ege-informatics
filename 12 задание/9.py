s = "7" * 61

while "777" in s or "73" in s:
    if "777" in s:
        s = s.replace("777", "73", 1)
    else:
        s = s.replace("73", "7", 1)

print(s)