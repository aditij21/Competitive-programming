def main():
    t = int(input())
    for _ in range(t):
        n= int(input())
        a=list(map(int, input().split()[:n]))
        ae=[]
        
        a.sort()
        if sum(a)%2==0:
            print(0)
        else:
            if 2 in a:
                print(1)
            else:
                print(-1)
    return 0
main()