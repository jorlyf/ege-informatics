"""
В первой строке - количество N (N <= 10**6).
Далее - последовательность из N целых чисел.
Каждое число положительное и <= 1000000.
Найти такую пару чисел, что их сумма минимальна и кратна 100.
Также в этой паре первый элемент должен быть не больше второго (элемент
пары, который встречается в последовательности раньше, должен быть
не больше элемента пары, который встречается позже).
"""

f = open("27 задание/1a.txt")
N = int(f.readline())

pr= [0] * 51
ps= [0] * 51
sm=[]
    
for i in range(N):
    x=int(f.readline())
    ost = x % 100
    if ost != 50:
       if ost<50 and (pr[ost]==0 or x<pr[ost]):
            pr[ost]=x
       if ost>50 and (ps[100-ost]==0 or x<ps[100-ost]):
           ps[100-ost]=x
    else:
       if (pr[50]==0 or x<pr[50]):
           pr[50]=x
       elif (ps[50]==0 or x<ps[50]):
           ps[50]=x

for i in range(0, 51):
    if pr[i]!=0 and ps[i]!=0:
        it=pr[i]+ps[i]
    else:
        it=0
    if it!=0:
       sm+=[it]

print(min(sm))
