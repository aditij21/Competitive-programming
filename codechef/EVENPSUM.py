import math
def main():
    t = int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        eva=math.floor(a/2)
        oda=math.ceil(a/2)
        evb=math.floor(b/2)
        odb=math.ceil(b/2)
        pair=(eva*evb)+(oda*odb)
        print (pair)
    return 0
main()