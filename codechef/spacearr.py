def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a=list(map(int, input().split()))
        c=0
        o=0
        a.sort()
        for i in range(len(a)):
            if a[i]>i+1:
                o=1
                break
            else:
                c+=(i+1)-a[i]
        if o==1:
            print("Second")
        elif c%2==0:
            print("Second")
        else:
            print("First")
    return 0
main()