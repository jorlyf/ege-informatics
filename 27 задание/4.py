"""
Найти макс сумму двух элементов последовательности, номера которых различаются не меньше чем на 5
"""

f = open("27 задание/4b.txt") # ответ: 14 для 4c.txt
N = int(f.readline())

буфер = []
for _ in range(5):
    буфер.append(int(f.readline()))

mx1 = 0
mxsum = 0
for _ in range(N-5):
    x = int(f.readline())
    mx1 = max(mx1, буфер[0])
    mxsum = max(mxsum, x+mx1)

    for i in range(4): # сдвигаю очередь
        буфер[i] = буфер[i+1]
    буфер[4] = x

    # print(буфер)
    # print(mx1, mxsum - mx1)
    
print(mxsum)