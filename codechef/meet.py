def times(c):
    o=0
    if "AM" in c:
        if c[:2]!="12":
            o=int(c[:2])*60+int(c[3:5])
        else:
            o=int(c[3:5])
    else:
        if c[:2]!="12":
            o=(int(c[:2])+12)*60+int(c[3:5])
        else:
            o=720+int(c[3:5])
    return o

t = int(input())
for _ in range(t):
    op=""
    p=input()
    p=times(p)
    n=int(input())
    for _ in range(n):
        time=input()
        l=times(time[:8])
        r=times(time[9:])
        if p>=l and p<=r:
            op+="1"
        elif r<l and p>=r and p<=l:
            op=+"1"
        else:
            op+="0"
    print(op) 