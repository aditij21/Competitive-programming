def main():
    t = int(input())
    for _ in range(t):
        n, k, l = [int(x) for x in input().split()]
        if n > k*l:
            print(-1)
        else:
            x = 1
            for i in range(n):
                if x > k:
                    x = 1
                print(x, end = " ")
                x += 1
            print()
    return 0

main()