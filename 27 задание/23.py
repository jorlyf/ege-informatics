"""
На вход программы поступает последовательность из целых положительных чисел.
Необходимо выбрать такую подпоследовательность подряд идущих чисел,
чтобы их сумма была максимальной и делилась на 43, а также её длину.
Если таких подпоследовательностей несколько,
выбрать такую, у которой длина меньше.
"""

f = open("27 задание/23b.txt")
N = int(f.readline())

d = 43
mx_sm = 0
sm = 0
ans_len = 0

m = [10**10] * d
l = [0] * d

for i in range(N):
    sm += int(f.readline())

    if sm % d == 0:
        if sm > mx_sm:
            mx_sm = sm
            ans_len = i + 1
        if sm == mx_sm:
            ans_len = min(i + 1, ans_len)

    sm1 = sm - m[sm%d]
    if sm1 > mx_sm:
        mx_sm = sm1
        ans_len = (i + 1) - l[sm%d]
    if sm1 == mx_sm:
        ans_len = min(i + 1, ans_len)

    if sm < m[sm%d]:
        m[sm%d] = sm
        l[sm%d] = i + 1

print(ans_len)