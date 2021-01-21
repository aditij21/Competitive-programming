def main():
    t = int(input())
    for _ in range(t):
        k,d0,d1=map(int,input().split())
        num=[d0,d1]
        if k==2:
            if sum(num)%3==0:
                print('YES')
            else:
                print('NO')
        if sum(num)%5==0:
            print('NO')
        elif k>=3:
            num.append(int(sum(num)%10))
            if k==3:
                if sum(num)%3==0:
                    print('YES')
                else:
                    print('NO')
            else:
                c=int(sum(num)%10)
                if c==2:
                    rep=[2,4,8,6]
                elif c==4:
                    rep=[4,8,6,2]
                elif c==8:
                    rep=[8,6,2,4]
                else:
                    rep=[6,2,4,8]
                rem=int((k-3)%4)
                if (sum(num+rep[:rem])+((k-3)//4)*20)%3==0:
                    print('YES')
                else:
                    print('NO')
    return 0
main()