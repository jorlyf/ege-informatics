"""
Из населенного пункта R в населенный пункт Q ведут две дороги.
Периодически между ними встречаются соединения.
Нужно найти минимальное расстояние из R в Q.
Тройки: 1 число - дорога А
        2 число - дорога B
        3 число - длина перемычки
"""

f = open("27 задание/7a.txt")
N = int(f.readline())

a1 = 0 
b1 = 0 # previous
for _ in range(N):
    a2, b2, s = map(int, f.readline().split())

    # if a1 + a2 < b1 + b2 + s:
    #     a3 = a1 + a2
    # else:
    #     a3 = b1 + b2 + s
    a3 = min(a1 + a2, b1 + b2 + s)
    
    # if b1 + b2 < a1 + a2 + s:
    #     b1 = b1 + b2
    # else:
    #     b1 = a1 + a2 + s
    b1 = min(b1 + b2, a1 + a2 + s)
    
    a1 = a3


print(a1, b1)
print(min(a1, b1))
