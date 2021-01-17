def main():
    t = int(input())
    for _ in range(t):
        k,d0,d1=map(int,input().split())
        num=[]
        num.append(d0)
        num.append(d1)
        for i in range(k):
            addnum=(num[i]+num[i+1]) % 10
            num.append(addnum)
        if sum(num)%3==0:
            print ("YES")
        else:
            print ("NO")
    return 0
main()