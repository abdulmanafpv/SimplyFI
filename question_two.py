def check(x,y):
    c=0
    for i in range(0,len(y)):
        if(x<y[i]):
            c+=1
    return c
for _ in range(int(input())):
    x=list(map(int,input().split()))
    l=list(map(int,input().split()))
    z=check(x[1],l)
    print(z)






