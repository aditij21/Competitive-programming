def main():
    t = int(input())
    for _ in range(t):
        n,x=map(int,input().split())
        op=0
        mr=0
        for _ in range(n):
            s,r=map(int,input().split())
            if s<=x:
                mr=r
            if mr>op:
                op=mr
        print(op)
    return 0
main()