def main():
    t = int(input())
    for _ in range(t):
        d,c=map(int,input().split())
        a=list(map(int, input().split()))
        b=list(map(int, input().split()))
        a1=sum(a)
        b1=sum(b)
        if sum(a)<150 and sum(b)<150:
            print("NO")
        else:
            if sum(a)>=150:
                a1=sum(a)+d
            if sum(b)>=150:
                b1=sum(b)+d
            if a1+b1>sum(a)+sum(b)+c:
                print("YES")
            else:
                print("NO")
    return 0
main()