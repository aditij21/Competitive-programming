t=int(input())
if t>0 and t<51:
    for i in range(t):
        n=int(input())
        if n>3 and n<65:
            if n==4: 
                matrix = [] 
                for i in range(4):          
                    a =[] 
                for j in range(4):      
                    a.append(int(input())) 
                matrix.append(a)
                for i in range(4):
                    for j in range(4):
                        c=(i-1).n+j
                        