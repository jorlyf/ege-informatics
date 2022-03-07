# На числовой прямой даны два отрезка: P=[2,10] и Q=[6,14]
# Какова максимальная длина отрезка A, при выборе которого формула
# ((x ∈ А) → (x ∈ P)) ∨ (x ∈ Q)
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.

def inP(x):
    return 20 <= x <= 100
def inQ(x):
    return 60 <= x <= 140
def inA(x, a1, a2):
    return a1 <= x <= a2

def f(x, a1, a2):
    return ((inA(x, a1, a2)) <= (inP(x))) or (inQ(x))

maxA = 0
for a1 in range(0, 151):
    for a2 in range(a1, 151):
        if all(f(x, a1, a2) for x in range(-500, 500)):
            maxA = max(maxA, a2-a1)

print(maxA / 10)
