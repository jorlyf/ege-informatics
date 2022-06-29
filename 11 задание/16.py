bit_symbol = 11
length = 23

V = 2050 * 2**10
# V = id_bytes * 65_536 <= 2050 * 2**10

print(V / 65_536) # 32 byte to one id
print(32*8 / 11)

print( ((bit_symbol * length // 8) + 1) * 65_536 / 2**10)