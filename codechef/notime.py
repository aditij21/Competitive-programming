def main():
    n,h,x=map(int,input().split())
    t=list(map(int, input().split()))
    op=0
    for i in range(len(t)):
        if x+t[i]>=h:
            op=1
    if op==0:
        print("NO")
    else:
        print("YES")
    return 0
main()