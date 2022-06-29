f = open("24 задание/15.txt")
s = f.readline()

#s = "AKPZRPQAZLMN"

# s = s.replace("PR", " ")
# s = s.replace("RP", " ")

# mx = max([len(sub) for sub in s.split()])
# print(mx+1)

mx = 0
current = ""
for i in range(len(s)):
    current += s[i]
    if "PR" not in current and "RP" not in current:
        mx = max(mx, len(current))
        #print(current)
    else:
        current = s[i]

print(mx)