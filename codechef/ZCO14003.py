n = int(input())
li = []
res = 0
for _ in range(n):
    k = int(input())
    li.append(k)
li.sort()
for i in range(n):
    tmp = li[i] * (n-i)
    if tmp > res:
        res = tmp
print(res)