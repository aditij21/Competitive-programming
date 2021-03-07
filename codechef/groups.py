def main():
    t = int(input())
    for _ in range(t):
        s=input()
        op=0
        a=s.split("0")
        a = list(filter(None, a)) 
        print(len(a))
    return 0
main()