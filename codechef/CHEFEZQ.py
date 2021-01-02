def main():
    t = int(input())
    count=0
    for _ in range(t):
        n, k = [int, input().split()]
        h=list(map(int, input().split()[:n]))
        for i in h:
            if h[i]>k:
                r=h[i]-k
                h[i+1]=h[i+1]+r
                i=i+1
                count=count+1
            else:
                count=1
        print (count)
    return 0
main()