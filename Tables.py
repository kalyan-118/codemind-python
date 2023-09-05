a,b=map(int,input().split())
c=1
for c in range(b+1):
    if c%2!=0:
        print(a,'x',c,'=',a*c)