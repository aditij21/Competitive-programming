def main():
    t = int(input())
    for _ in range(t):
        n= int(input())
        op=0
        for _ in range(n):
            s,p,v=map(int,input().split())
            s+=1
            profit=(p//s)*v
            if profit>op:
                op=profit
        print (op)
    return 0
main()