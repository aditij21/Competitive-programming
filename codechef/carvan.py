def main():
    t = int(input())
    for _ in range(t):
        n=int(input())
        s=list(map(int, input().split()))
        i=0
        ms=s[0]
        op=0
        for i in range(n):
            if s[i]<=ms:
                op+=1
                ms=min(ms,s[i])
        print(op)
    return 0
main()