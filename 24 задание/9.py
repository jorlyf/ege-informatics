f = open("24 задание/9.txt")
s = f.readline()

s = s.replace("AB", "*")
s = s.replace("AC", "*")

s = s.replace("A", " ")
s = s.replace("B", " ")
s = s.replace("C", " ")

print(max(len(sub) for sub in s.split()))