def main():
    t = int(input())
    for _ in range(t):
        w1,w2,x1,x2,m=map(int,input().split())
        ran=list(range(min(x1,x2)*m,max(x1,x2)*m+1))
        if w2-w1 in ran:
            print(1)
        else:
            print(0)
    return 0
main()