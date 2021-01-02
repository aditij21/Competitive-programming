import math
def main():
    t = int(input())
    for _ in range(t):
        n,d=map(int,input().split())
        a=[int(x) for x in input().split()]
        risk=[]
        for i in a:
            if i<10 and i>79:
                risk.append(i)
        no_risk = [i for i in a if i not in risk]
        td=math.ceil(len(risk)/d)+math.ceil(len(no_risk)/d)
        print (td)
    return 0
main()