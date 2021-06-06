n=int(input())
if n%5==0 and n%11==0:
    print ("BOTH")
elif n%5!=0 and n%11!=0:
    print ("NONE")
else:
    print ("ONE") 