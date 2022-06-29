def f(x):
    K = 9*x - 57
    D = 9*x + 13
    while K*D > 0:
        if K>D:
            K = K % D
        else:
            D = D % K
    
    return K + D

for x in range(1, 1000):
    if f(x) == 70:
        print(x)