n=int(input())
num=list(map(int,input().split()))
s=0
s1=0
for i in num:
    if i%2==0:
        s=s+i
    else:
        s1=s1+i
print(abs(s1-s))