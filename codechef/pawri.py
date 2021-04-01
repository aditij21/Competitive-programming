def main():
    t = int(input())
    for _ in range(t):
        s=input()
        if "party" in s:
            s=s.replace("party","pawri")
        print(s)
    return 0
main()