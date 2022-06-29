f = open("24 задание/11.txt")
ips = [x for x in f.readlines()]

cnt = 0
# 195.2?.1?5.14
for ip in ips:
    ip = ip[:-1]
    for i in "0123456789":
        for j in "0123456789":
            nIP = f"195.2{i}.1{j}5.14"
            #print(ip, nIP)
            if nIP == ip:
                cnt += 1

print(cnt)