f = open("24 задание/14.txt")
s = f.readline()

mxsm = 0
sm = 0
flagZero = True
for i in range(len(s)-1):
    if flagZero:
        if s[i] == "0":
            sm += 1
        else:
            mxsm = max(mxsm, sm)
            sm = 0
        if s[i+1] == "1":
            flagZero = False
    else:
        if s[i] == "1":
            sm += 1
        else:
            mxsm = max(mxsm, sm)
            sm = 0
            flagZero = True

print(mxsm)