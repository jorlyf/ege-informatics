"""
У исполнителя есть команды, которым присвоены номера:
1. Прибавить 2
2. Умножить на 3
Сколько разных чисел может быть получено из числа 2 с помощью программ,
состоящих из 3 команд?
"""
dict = set()
def f(x, step):
    if step == 0: dict.add(x); return
    f(x+2, step-1)
    f(x*3, step-1)

f(2, 3)
print(len(dict))


def f(x, step, dict):
    if step == 3: return dict + [x]
    return f(x+2, step+1, dict) + f(x*3, step+1, dict)

print(len(set(f(2, 0, []))))
