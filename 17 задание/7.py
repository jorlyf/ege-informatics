f = open("17 задание/7.txt")
a = [int(num) for num in f.readlines()]
f.close()

s = [x for x in a\
    if x % 3 == 0 and\
        x % 7 != 0 and\
        x % 17 != 0 and\
        x % 19 != 0 and\
        x % 27 != 0]
        
print(len(s), max(s))
