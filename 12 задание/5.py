def f(s):
    while "55555" in s:
        s = s.replace("55555", "88", 1)
        s = s.replace("888", "55", 1)

    return s

mx_cnt = 0
min_len = 0
for len in range(301, 100000):
    cnt_5 = f("5"*len).count("5")
    #print(len, f("5"*len))
    if mx_cnt < cnt_5:
        mx_cnt = cnt_5
        min_len = len
        print(mx_cnt, min_len)