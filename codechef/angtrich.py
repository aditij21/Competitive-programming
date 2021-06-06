a,b,c=map(int, input().split())
if a+b+c!=180 or a==180 or b==180 or c==180 or a==0 or b==0 or c==0:
    print("NO")
else:
    print("YES")