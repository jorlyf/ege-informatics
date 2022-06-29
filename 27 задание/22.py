# Набор данных представляет собой последовательность натуральных чисел.
# Необходимо выбрать такую подпоследовательность подряд идущих чисел,
# чтобы их сумма была максимальной и делилась на 69, и определить её длину.

# file A = 14
# file B = 99989

# f = open("27 задание/22b.txt")
# N = int(f.readline())

# ans_len = 0
# d = 69
# mx_sum = 0

# a = [int(f.readline()) for _ in range(N)]

# for i in range(N):
#     sm = 0
#     cur_len = 0
#     for j in range(i, N):
#         sm += a[j]
#         cur_len += 1

#         if sm % 69 == 0:
#             if sm > mx_sum:
#                 mx_sum = sm
#                 ans_len = cur_len

#     if i % 1_000 == 0:
#         print(f"{i}/100000")

# print(ans_len)

f = open("27 задание/22b.txt")
N = int(f.readline())

d = 69
ans_len = -1
mx_sm = 0

m = [10**20] * d
l = [0] * d

sm = 0
cur_len = 0
for i in range(N):
    sm += int(f.readline())

    if sm % d == 0:
        if sm > mx_sm:
            mx_sm = sm
            ans_len = i + 1

    sm1 = sm - m[sm%d]
    if sm1 > mx_sm:
            mx_sm = sm1
            ans_len = (i + 1) - l[sm%d]

    if sm < m[sm%d]:
        m[sm%d] = sm
        l[sm%d] = i + 1

print(ans_len)
    