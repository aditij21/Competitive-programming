def main():
    t = int(input())
    for _ in range(t):
        n=int(input())
        c=list(map(int, input().split()[:n]))
        if (max(c)>=sum(c)-max(c)):
            minute=max(c)
        elif (max(c)+min(c)>sum(c)-(max(c)+min(c))):
            minute=sum(c)-max(c)
        else:
            minute=sum(c)-max(c)-min(c)
        print(minute)
    return 0
main()