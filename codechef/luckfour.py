t=int(input())
for i in range (t):
    n=input()
    count=0
    for i in n:
        if int(i)==4:
            count+=1
    print(count)