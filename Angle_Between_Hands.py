a,b=map(int,input().split(':'))
if a==12:
    a=0
if b==60:
    b=0
ag=0.5*(a*60+b)
bn=6*b
vk=abs(ag-bn)
print(min(360-vk,vk))
