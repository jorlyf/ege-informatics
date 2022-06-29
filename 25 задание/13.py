# < 10^9

d = []

s = int("1234576") # % 73 = 0
d.append(s)
for q1 in range(10):
    s = int(f"12345{q1}76")
    if s % 73 == 0:
        d.append(s)

for q1 in range(10):
    for q2 in range(10):
        s = int(f"12345{q1}{q2}76")
        if s % 73 == 0:
            d.append(s)

for q1 in range(10):
    for q2 in range(10):
        for q3 in range(10):
            s = int(f"12345{q1}{q2}{q3}76")
            if s % 73 == 0:
                d.append(s)

d.sort()
print(d[:5])