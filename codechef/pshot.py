def main():
    t = int(input())
    for _ in range(t):
        n=int(input())
        s=input()
        score=list(map(int,n))  
        count=0
        as=0
        bs=0
        for i in score:
            if i%2==0:
                if i==1:
                    as+=1
                    if as==(2*n)-2:
                        count=as
            else:
                if i==1:
                    bs+=1
                    if bs==(2*n)-2:
                        count=bs
        if count==0:
            print(2*n)
    return 0
main()