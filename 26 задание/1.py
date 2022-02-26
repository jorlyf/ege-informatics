f = open("26 задание/1.txt")
countProducts = 7598
countBuyers = 7759

allNums = []
for i in f.readlines():
    allNums.append(int(i))

print(allNums)