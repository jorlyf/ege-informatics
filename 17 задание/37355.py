# В файле содержится последовательность из 10 000 целых положительных чисел.
# Каждое число не превышает 10 000. Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых сумма элементов кратна 7, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности.
# Порядок элементов в паре не важен.

f = open("17 задание/37355.txt")
lines = f.readlines()

mxsum = -1000000
count = 0

for i in range(0, len(lines)):
  for j in range(i, len(lines)):
    if (int(lines[i]) + int(lines[j])) % 7 == 0:
      count += 1
      mxsum = max(mxsum, int(lines[i]) + int(lines[j]))

print(count, mxsum)
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
