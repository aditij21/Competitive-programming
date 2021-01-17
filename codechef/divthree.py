import math
def main():
    t = int(input())
    for _ in range(t):
        n,k,d=map(int,input().split())
        a=list(map(int, input().split()))
        summ=sum(a)
        op=0
        if summ<k:
            op=0
        else:
            div=math.floor(summ/k)
            if div<d:
                op=div
            else:
                op=d
        print (op)
    return 0
main()