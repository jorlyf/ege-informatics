"""
У исполнителя Калькулятор есть три команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 5
3. Умножить на 3
Сколько разных чисел может быть получено из числа 1 с помощью программ, состоящих из 7 команд?
"""
dict = set()
def f(x, step):
    if step == 0: dict.add(x); return
    f(x+1, step-1)
    f(x+5, step-1)
    f(x*3, step-1)

f(1, 7)
print(len(dict))

def f(x,step,res=[]):
    if step == 7:
        return res+[x]  
    return f(x+1,step+1,res)+f(x+5,step+1,res)+f(x*3,step+1,res)
print(len(list(set(f(1,0,[])))))

