from math import log2

вариантов_значений = 4 # / 1 2 3 - /
кол_во_ячеек = 20 * 10

бит_информации_всего = кол_во_ячеек * log2(вариантов_значений)
print(бит_информации_всего)