def main():
    t = int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int, input().split()))
        op=0
        a.sort()
        x=a[0]
        y=a[1]
        z=a[-1]
        op=abs(x-y)+abs(y-z)+abs(z-x)
        print (op)
    return 0
main()