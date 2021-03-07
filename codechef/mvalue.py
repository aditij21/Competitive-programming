def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a=list(map(int, input().split()))
        a.sort()
        m=a[0]*a[1]+abs(a[0]-a[1])
        n=a[-1]*a[-2]+abs(a[-1]-a[-2])
        op=max(m,n)
        print(op)
    return 0
main()