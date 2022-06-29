f = open("24 задание/8.txt")

s = f.readline()
f.close()

min_len = 1000000
min_a = ""

#s = "BACDFBDCFCDBFDABC"
s = s.split("F")
for w in s:
    a = ""
    for i in range(len(w)):
        a += w[i]
    if len(a) <= min_len:
        min_len = len(a)
        min_a = a

print(min_len)
print(min_a)