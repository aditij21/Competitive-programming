def main():
    t = int(input())
    for _ in range(t):
        a=list(map(int, input().split()))
        k=int(input())
        op=0
        if k==0 or k<a[-1]:
            print(len(a))
        else:
            for _ in a:
                if k!=0:
                    a[-1]=a[-1]-k
                    k=k-a[-1]
                    del a[-1]
                    op=len(a)
        print(op)
    return 0
main()