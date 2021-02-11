def main():
    t = int(input())
    for _ in range(t):
        n=int(input())
        s=int(input())
        score=list(map(int, str(s)))    
        a=b=am=bm=0
        count=0
        for i in range(len(score)):
            if i%2==0:
                if score[i]==1:
                    a+=1
                else:
                    am+=1
            else:
                if score[i]==1:
                    b+=1
                else:
                    bm+=1
            if a>n-bm or b>n-am:
                count=1
                print(i+1)
                break 
        if count==0:
            print(2*n)
    return 0
main()