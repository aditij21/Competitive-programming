def main():
    t = int(input())
    for _ in range(t):
        n,m=map(int, input().split())
        o=pow(2,n,1000000007)-1
        op=(pow(o,m,1000000007))
        print(op)
    return 0
main()