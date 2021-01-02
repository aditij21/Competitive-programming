def main():
    n,m=map(int,input().split())
    a=list(map(int, input().split()[:n]))
    b=list(map(int, input().split()[:m]))
    count=0
    mini=min(a)
    a.remove(min(a))
    a.insert(0,mini)
    b.sort()
    for i in b: 
        if i > mini : 
            count=count+1
    op=count*len(a)
    print(op)
    return 0
main()