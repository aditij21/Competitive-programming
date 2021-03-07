def main():
    t = int(input())
    for _ in range(t):
        s = int(input())
        q=list(map(int, input().split()))
        op=0
        for j in range(s):
            e=list(map(int, input().split()))
            del(e[0])
            e = [x-q[j] for x in e]
            op += sum(e) + q[j]
        print(op)
    return 0
main()