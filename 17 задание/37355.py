f = open("17 задание/37355.txt")
data = []

for element in f:
    data.append(int(element))

counter = 0
maximum = 0

for i in range(len(data)):
    for j in range(len(data)):
        if (data[i] + data[j]) % 7 == 0:
            counter += 1
            maximum = max(maximum, data[i] + data[j])

print(counter, maximum)