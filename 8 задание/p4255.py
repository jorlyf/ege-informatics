# Мила составляет 4-значные числа в 8-ичной системе.
# Сколько различных чисел, делящихся на 4 без остатка, может составить Мила?

import itertools
nums = list(itertools.product("01234567", repeat=4))

count = 0
for num in nums:
  num = "".join(num)
  if (num[0] == "0"): continue

  intnum = int(num, 8)
  if intnum % 4 == 0:
    count += 1

print(count)
