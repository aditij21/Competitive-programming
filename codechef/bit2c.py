t=int(input())
if t>0 and t<100:
    for i in range(t):
        n, k = map(int,input().split())
        sum=0
        if n>0 and n<10001 and k>0 and k<1001:
            l= list(map(int,input().split()))
            if len(l)>0 & len(l)<1001:
                for i in range(n):
                    if l[i]>k:
                        sum+=l[i]-k
                print(sum)
            else:
                exit()
        else:
            exit()
else:
    exit()