#На числовой прямой даны два отрезка: P = [25; 50] и Q = [32; 47]. Укажите наибольшую возможную длину промежутка A, для которого формула
#(¬ (x e A) → (x e P)) → ((x e A) → (x e Q))
#тождественно истинна, то есть принимает значение 1 при любом значении переменной х

A = [a for a in range(25, 50+1)]

P = [x for x in range(25, 50+1)]
Q = [x for x in range(32, 47+1)]

for a in range(25, 50+1):
  for x in range(-100, 100):
    if not ((not (x in A) <= (x in P)) <= ((x in A) <= (x in Q))):
      A.remove(a)
      break

print(A)
