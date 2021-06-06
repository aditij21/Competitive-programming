n=int(input())
l=list(map(int, input().split()[:n]))
l.reverse()
print(' '.join(map(str,l)))