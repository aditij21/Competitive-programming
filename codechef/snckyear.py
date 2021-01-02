T = int(input())
if T>=1 and T<=51:
    for i in range(T):
        n=int(input())
        if n>0 and n<100001:
            h=list(map(int, input().split()))
            s=set(h)
            print(len(s))