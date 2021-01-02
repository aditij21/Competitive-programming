def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        if (n==k):
            for i in range(n):
                print (i)
        elif (n<k/2):
            print("even")
        else:
            print("odd")

    return 0
main()