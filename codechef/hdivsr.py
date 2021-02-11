n=int(input())
i = 1
op=[]
while i <= 9 : 
    if (n % i==0) : 
         op.append(i)
    i=i+1
print (op[-1])