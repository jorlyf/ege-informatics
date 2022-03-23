a=[]
f=open("27 задание/4a.txt")
n=int(f.readline())
k=5
for i in range(k):
    a+=[int(f.readline())]
    
mx=0
mxsm=0
for i in range(k,n):
    ch = int(f.readline())
    if a[0] > mx:
        mx=a[0]
    if mxsm < mx+ch:
        mxsm=mx+ch

    for j in range(k-1):
        a[j]=a[j+1]
    a[k-1]=ch
    print(a)

print(mxsm)
print(mx, mxsm - mx)
