def main():
    t = int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        h=list(map(int, input().split()))
        h.sort(reverse=True)
        i=0
        j=1
        s1=0
        s2=0
        op=0
        if sum(h)<2*k:
            print(-1)
        for i in range(n):
            while s1<k:
                s1=s1+h[i]
                i+=2
                op=op+1
        for j in range(n):
            while s2<k:
                s2=s2+h[j]
                j+=2
                op=op+1
        print (op)
    return 0
main()