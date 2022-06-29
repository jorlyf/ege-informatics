a = 39 * 15**64 + 35**450 + 74 * 43**121 - 450035

print(str(a).count("8"))

for base in range(2, 15):
    cnt8 = 0
    m = a
    while m > 0:
        if m % base == 8: cnt8 += 1
        m //= base
    print(base, cnt8)