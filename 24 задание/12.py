f = open("24 задание/12.txt")
s = f.readline()

s = s.replace("AB", "*")
s = s.replace("CAC", "*")
s = s.replace("A", " ")
s = s.replace("B", " ")
s = s.replace("C", " ")

a = s.split()
print(max([len(x) for x in a]))