import math
def main():
    t = int(input())
    for _ in range(t):
        c = int(input())
        d=math.log(c)/math.log(2)
        if (d*10)%10==0:
            d=int(d)+1
        d1=math.ceil(d)
        x=(2**d1)
        x=bin(x)[2:]
        c=bin(c)[2:]
        c=str(c)
        a=[]
        b=[]
        for i in range(len(x)-1):
            b.append("1")
            if c[i]=="1":
                a.append("0")
            else:
                a.append("1")
        b.pop(0)
        a.pop(0)
        b.insert(0,"0")
        a.insert(0,"1")
        a=''.join(map(str,a))
        b=''.join(map(str,b))
        a=int(a,base=2)
        b=int(b,base=2)
        print(a*b)
    return 0
main()