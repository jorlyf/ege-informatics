# Набор данных представляет собой последовательность натуральных чисел.
# Необходимо найти количество подпоследовательностей подряд идущих чисел,
# чтобы их сумма делилась на 71.

# file A = 17
# file B = 70416562

# f = open("27 задание/20b.txt")
# N = int(f.readline())

# a = [int(f.readline()) for _ in range(N)]
# f.close()

# cnt = 0
# for i in range(0, N):
#     sm = 0
#     for j in range(i, N):
#         sm += a[j]
#         if sm % 71 == 0:
#             cnt += 1

#     if i % 1000 == 0:
#         print(f"{i}/{100_000}")
  
# print(cnt)

f = open("27 задание/20b.txt")
N = int(f.readline())
ln = [0] * 71
sm = 0

cnt = 0
for i in range(N):
    sm += int(f.readline())
    if sm % 71 == 0:
        cnt += 1
    
    cnt += ln[sm%71]

    ln[sm%71] += 1

print(cnt)