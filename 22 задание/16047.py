# вывод: 21 3

for w in range(1, 1000):
  x = w
  L = 1
  M = 0
  while x > 0:
    M = M + 1
    if x % 2 != 0:
      L = L * (x % 8)
    x = x // 8
  if (L, M) == (21, 3):
    print(w) # max is 499