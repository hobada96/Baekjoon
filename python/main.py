    *l,S=map(int,input().split())
    a,b=max(l),min(l)
    n=a==0 and 1 or S//a-1
    m=(S-a*n)//b
    while True:
        s=(S-a*n+b*m)
        print(n,m,s)
            
        if n==0 or m==0:
            print("NO")
            break
        elif (a*n+b*m)==S:
            print("YES")
            break
        else:
            if s%b!=0:
                n-=1
                m+=(S-a*n+b*m)//b
            else:
                m+=(S-a*n+b*m)//b