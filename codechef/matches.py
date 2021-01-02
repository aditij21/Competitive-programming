t=int(input())
arr=[6,2,5,5,4,5,6,3,7,6]
for i in range(t):
    a,b=map(int,input().split())
    sum=0
    x=a+b
    while x:
        sum+=arr[x%10]
        x=int(x/10)
    print(sum)