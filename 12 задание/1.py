# ПОКА нашлось (111)
#    заменить(111, 2)
#    заменить(222, 3)
#    заменить(333, 1)
# КОНЕЦ ПОКА

s = "1" * 130
while "111" in s:
    s = s.replace("111", "2", 1)
    s = s.replace("222", "3", 1)
    s = s.replace("333", "1", 1)

print(s)