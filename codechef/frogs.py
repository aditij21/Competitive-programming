import math
def main():
    t = int(input())
    for _ in range(t):
        n= int(input())
        w=list(map(int, input().split()[:n]))
        l=list(map(int, input().split()[:n]))
        op=0
        ind={}
        if w==sorted(w):
            print(op)
        else:
            for i in range(1,n+1):
               ind[i]=w.index(i)
            for i in range(2,n+1):
               t2=ind[i]
               t1=ind[i-1]
               t=0
               if t2<=t1:
                    t=math.ceil((t1+1-t2)/l[t2])
        op+=t
        ind[i]+=t*(l[t])
        print(op)
    return 0
main()