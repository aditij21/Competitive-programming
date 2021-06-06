n = int(input())
lo=[]
le=[]
for i in range(1, (2*n)+1):
    if i%2==0:
        le.append(i)
    else:
        lo.append(i)
print(sum(lo),sum(le))