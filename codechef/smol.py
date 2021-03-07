def main():
    t = int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        if k==0:
            print(n)
        else:
            print(n%k)
    return 0
main()