def main():
    t = int(input())
    for _ in range(t):
        n,k,x1,y1=map(int,input().split())
        a=[]
        if x1==y1:
            print(n,n)
        else:
            if x1<y1:
                c1=[x1+n-y1,n]
                c2=[n,x1+n-y1]
                c3=[y1-x1,0]
                c4=[0,y1-x1]
            else:
                c1=[n,y1+n-x1]
                c2=[y1+n-x1,n]
                c3=[0,x1-y1]
                c4=[x1-y1,0]
            res=[c1,c2,c3,c4]
            ans=res[(k-1)%4]
            print (ans[0],ans[1])
    return 0
main()