t = int(input())
if t>=1 and t<=256:
    for i in range(t):
        n,k = map(int,input().split())
        if n>=2 and k>=0 and n<=20 and k<=n-1:
            for i in range(k+1) :
                print(n-k + i),
            for i in range(1, n-k) :
                print(i)