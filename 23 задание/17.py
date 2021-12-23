dict = set()
def f(x, step):
    dict.add(x)
    if step == 0: return
    f(x+1, step-1)
    f(x*2, step-1)

f(1, 4)
print(len(dict) - 1) # -1, чтоб не считать первое ни о чем
