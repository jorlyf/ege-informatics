len1 = 16
bit1 = 5

v1 = bit1 * len1

len2 = 15
bit2 = 4

v2 = bit2 * len2

#print(v1 + v2) #140

byte = (v1 + v2) // 8 + 1 # 18

print((18592 - 56*byte) / 56)