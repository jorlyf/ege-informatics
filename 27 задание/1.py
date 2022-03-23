f = open("27 задание/1a.txt")
N = int(f.readline())

числа = [0] * 100
остатки = [0] * 100
for i in range(N):
    числа.append(int(f.readline()))
    остатки.append(числа[i] % 100)

# сумма = 2**32
# for j in range(N):
#     if остатки[j] == 0:
#         ...
#     else:
#         остаток1 = остатки[j]
#         остаток2 = остатки[100 - j]
