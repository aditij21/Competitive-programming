for _ in range(int(input())):
    num=int(input())

    count=0
    i=5
    while(num/i>=1):
        count+=(num//i)
        i*=5
        
    print(count)