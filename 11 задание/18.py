bit_symbol = 4
bit_psw = bit_symbol * 11
byte_psw = bit_psw // 8 + 1 # 6

V_30 = 840 #byte
V = V_30 // 30 # 28
print(V - 4 - byte_psw)