def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

for x in range(2, 43):
    a = 381
    print(x, convert_base(a, x))