def main():
    t = int(input())
    for _ in range(t):
        n=input()
        e=0
        o=0
        a,b=map(int,input().split())
        for i in range(len(n)):
            if i % 2 == 0:
                o += int(n[i])
            else:
                e += int(n[i])
        s=o*a+e*b
        while s>9:
            s=str(s)
            l=list(map(int,s.strip()))
            s=sum(l)
        print(s)
    return 0
main()