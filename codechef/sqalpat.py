n=int(input())
k=-4
for i in range(1, n+1):
    if (i%2!=0):
        k+=4
        for j in range (1,6):
            print (k+1,end=" ")
            k+=1
        print()
    else:
        k+=4
        for j in range(1,6):
            print (k+1,end=" ")
            k-=1
        k+=2
        print()