def main():
    d1,v1,d2,v2,p=map(int,input().split())
    sum=0
    count=0
    count1=0
    count2=0
    s=0
    for i in range(1000):
        if i>=d1:
            sum=sum+v1
            count+=1
            count1+=1
        if i>=d2:
            s=s+v2
            count+=1
            count2+=1
        if sum+s>=p:
            break
    if d1>d2:
        count=count-count1+d2-1
    else:
        count=count-count2+d1-1
    print (count)
    return 0
main()