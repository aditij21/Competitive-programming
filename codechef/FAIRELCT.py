def main():
    t = int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        a=list(map(int, input().split()))
        b=list(map(int, input().split()))
        op=0
        flag=True
        while sum(a)<=sum(b):
            a.sort()
            b.sort()
            if a[0]<b[-1]:
                t=b[-1]
                b[-1]=a[0]
                a[0]=t
                op=op+1
            else:
                flag=False
                print(-1)
                break
        if flag==True:
            print(op)
    return 0
main()