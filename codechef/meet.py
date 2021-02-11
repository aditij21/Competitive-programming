import re
def main():
    t = int(input())
    for _ in range(t):
        p=input()
        n=int(input())
        for _ in range(n):
            i=input()
            l,r=re.split('AM PM',i)
            print (l,r)
    return 0
main()