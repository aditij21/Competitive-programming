def main():
    t = int(input())
    for _ in range(t):
        D,d,p,q=map(int, input().split())
        op=0
        if (D//d)%2==0:
            op+=d*(((D//d)//2)*(2*p+((D//d)-1)*q))
        else:
            op+=d*((D//d)*(p+(((D//d)-1)//2)*q))
        op+=(D%d)*(p+(D//d)*q)
        print(op)
    return 0
main()