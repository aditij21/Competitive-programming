def main():
    t = int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        d=-(-n//k)
        x=int(n%k)
        if x==0:
            x=k
        print(d,x)
    return 0
main()