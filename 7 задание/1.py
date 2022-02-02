v = 2**22 # скорость бит/с
v_kanal = 2**19 # скорость канала бит/с
s = 2**23 * 8 # объем файла

step = 2**13 * 512 # ретрансляция по каналу начнется после загрузки 512КБ
t1 = s / v
print(t1)

stepSuccessAfterT = step / v
print(stepSuccessAfterT)

t2 = s / v_kanal
print(t2)

answ = t2 + stepSuccessAfterT
print(answ) # 129