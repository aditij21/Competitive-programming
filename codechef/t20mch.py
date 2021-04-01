def main():
    r,o,c=map(int,input().split())
    rem=20-o
    run=rem*36
    if run+c>r:
        print("YES")
    else:
        print("NO")
    return 0
main()