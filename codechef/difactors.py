n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print (len(l))
print (' '.join(map(str,l)))