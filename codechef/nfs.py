def main():
    t = int(input())
    for _ in range(t):
        u,v,a,s=map(int,input().split())
        l=[]
        if u==v or u<v:
            print("Yes")
        else:
            if u*u-2*a*s<=v*v:
                print("Yes")
            else:
                print("No")
    return 0
main()