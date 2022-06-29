s = "2" * 400
while "8888" in s or "222" in s:
    if "222" in s:
        s = s.replace("222", "88", 1)
    else:
        s = s.replace("8888", "22", 1)

print(s)