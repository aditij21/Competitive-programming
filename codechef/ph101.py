def main():
    t = int(input())
    for _ in range(t):
        n=input()
        c=0
        for i in range(len(n)):
            if n[i]=="7":
                c=1
        if c==1:
            print("True")
        else:
            print("False")
    return 0
main()