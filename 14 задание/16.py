a = 80 - 27**7 + 9**15
# cnt = 0
# while a > 0:
#     ost = a % 3
#     if ost == 2:
#         cnt += 1
#     a = a // 3
# print(cnt)

s = ""
while a > 0:
    s = str(a % 3) + s
    a = a // 3
print(s.count("2"))