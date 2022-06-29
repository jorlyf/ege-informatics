s = "5" * 70

while "555" in s or "444" in s:
    if "555"in s:
        s = s.replace("555", "4", 1)
    else:
        s = s.replace("444", "5", 1)

print(s)