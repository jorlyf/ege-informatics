множество = sorted(set(x for x in range(1425, 9605+1) 
if ((x % 3 == 0 or x % 4 == 0) and (x % 5 != 0 and x % 7 != 0 and x % 9 != 0))))

print(множество[100-1])
print((9605+1 - 1425) - len(множество))