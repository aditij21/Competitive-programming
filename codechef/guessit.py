def main():
    l=1
    u=10**6
    list=[]
    c=0
    for i in range(l,u+1):
        if (i**(.5) == int(i**(.5))):
            list.append(i)

    t = int(input())
    for _  in range(t):
        for i in list:
            print(i,flush=True)
            resp=int(input())
            if resp == 1:
                break
            if resp == -1:
                return 0
    return 0
main()