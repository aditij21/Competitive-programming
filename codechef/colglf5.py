def main():
    t = int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        f=list(map(int, input().split()[:n]))
        c=list(map(int, input().split()[:m]))
        op=0
        s=[]
        t=f+c
        t.sort()
        for i in t:
            if i in f:
                s.append("f")
            else:
                s.append("c")
        temp="f"
        for i in s:
            if temp=="f":
                if i=="c":
                    op+=1
                    temp="c"
            else:
                if i=="f":
                    op+=1
                    temp="f"
        print(op)
    return 0
main()