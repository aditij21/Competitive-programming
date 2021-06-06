def main():
    t = int(input())
    for _ in range(t):
        xml,xg,Xa,Xb=map(int, input().split())
        op=(Xa/xml)+(Xb/xg)
        print(int(op))
    return 0
main()