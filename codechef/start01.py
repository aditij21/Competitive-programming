try:
    t=int(input())
    if t>0 and t<51:
        for i in range(t):
            n=int(input())
            if n>0 and n<100001:
                h=list(map(int, input().split()))
                s=set(h)
                print(len(s))
except:
    exit()