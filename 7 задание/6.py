dpi = 300
x = 3 * dpi
y = 4 * dpi

color_bits = 16
V_header = 4 * 2**13

a = (x*y*color_bits + V_header)
b = a / 2**13
print(b)