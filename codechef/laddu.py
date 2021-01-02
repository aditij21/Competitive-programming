for _ in range(int(input())):
    activity,country=input().split()
    laddu=0
    activity=int(activity)
    for i in range(activity):
        act=input().split()
        if act[0]=='CONTEST_WON':
            laddu+=300
            rank=int(act[1])
            if rank<=20:
                laddu+=(20-rank)
        elif act[0]=='TOP_CONTRIBUTOR':
            laddu+=300
        elif act[0]=='BUG_FOUND':
            severity=int(act[1])
            laddu+=severity
        elif act[0]=='CONTEST_HOSTED':
            laddu+=50
    if country=='INDIAN':
        print(laddu//200)
    else:
        print(laddu//400)