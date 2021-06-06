def main():
    t = int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        f=list(map(int, input().split()[:n]))
        c=list(map(int, input().split()[:m]))
        f1 = []
        for i in range(n):
            f1.append([f[i], 0])
        c1 = []
        for i in range(m):
            c1.append([c[i], 1])

        allList = f1 + c1
        allList.sort()

        cnt = 0
        flag = 0

        for i in range(len(allList)):
            if flag != allList[i][1]:
                flag = allList[i][1]
                cnt += 1

        print(cnt)
    return 0
main()