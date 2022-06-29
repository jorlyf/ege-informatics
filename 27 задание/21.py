"""
На вход программы поступает последовательность из целых положительных чисел.
Необходимо выбрать такую подпоследовательность подряд идущих чисел,
чтобы их сумма была максимальной и делилась на 93 и была нечётной.
Укажите сумму.

file A = 19437
file B = 50225208
"""

f = open("27 задание/21b.txt")
N = int(f.readline())

d = 93

sums = [10**10] * d

sm = 0
mx_sm = 0
for i in range(N):
    x = int(f.readline())
    sm += x
    
    if sm % d == 0 and sm % 2 != 0:
        mx_sm = max(mx_sm, sm)

    sm1 = sm - sums[sm%d]
    if sm1 % 2 != 0:
        mx_sm = max(mx_sm, sm1)
    
    sums[sm%d] = min(sums[sm%d], sm)

print(mx_sm)
