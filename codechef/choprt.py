T = int(input())
if T>=1 and T<=1000:
    for _ in range(T):
        N,K = map(int,input().split())
        if N>=1 and K>=1 and N<=1000000001 and K<=1000000001:
            if N>K:
                print(">")
            elif N<K:
                print("<")
            else:
                print("=")