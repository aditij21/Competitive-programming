T = int(input())
if T>=1 and T<=100:
    for _ in range(T):
        N,K = map(int,input().split())
        if N>=1 and K>=1 and N<=10000 and K<=1000:
            P = list(map(int,input().split()))
            np = 0
            cp = 0
            if sum(P)>=1 and sum(P)<=1000*N:
                for i in P:
                    np += i
                    if i>K:
                        i=K
                    cp += i
                print(np-cp)
