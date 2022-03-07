f = open("24 задание/3.txt")
a = f.readline()

словарь = dict()
for i in range(0, len(a)):
    if a[i] == "X" and a[i+2] == "Z": 
        if a[i+1] in словарь:
            словарь[a[i+1]] += 1
        else:
            словарь[a[i+1]] = 1

mx = 0
for key in словарь:
    if словарь[key] > mx:
        mx = словарь[key]

print(mx)