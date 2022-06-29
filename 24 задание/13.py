f = open("24 задание/13.txt")
s = f.readline()

#s = "PPQPPRSPQQQPPPPPPPRSSSSPPPPPPPS"

mx = 0
cmx = 0
for i in range(len(s) - 1):
    cmx += 1
    if s[i] == "P" and s[i+1] == "P":
        mx = max(mx, cmx)
        cmx = 0

print(mx)
# PQRSPQQQPPRS
