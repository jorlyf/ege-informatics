f = open("24 задание/6.txt")
s = f.readline()
f.close()

max_len = 0
max_array = ""
current = ""
for i in range(len(s)):
    current += s[i]
    if "PR" in current and "ST" in current:
        current = s[i]
    else:
        max_len = max(max_len, len(current))
        if len(current) > len(max_array):
            max_array = current

print(max_len)
print(max_array)