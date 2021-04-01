def main():
    t = int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        a=list(map(int, input().split()[:n]))
        a=set(a)
        if len(set(a))<m:
            print("Yes")
        else:
            print("No")
    return 0
main()