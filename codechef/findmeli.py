n,k=map(int,input().split())
l=list(map(int, input().split()[:n]))    
if k in l:
    print("1")
else:
    print("-1")