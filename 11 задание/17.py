ln = 15
bit_symbol = 3

bit_psw = ln * bit_symbol
byte_psw = bit_psw // 8 + 1 # 6

V = (byte_psw + 24) * 20
print(V)