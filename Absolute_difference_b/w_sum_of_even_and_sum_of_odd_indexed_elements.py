n=int(input())
num=list(map(int,input().split()))
s=0
s1=0
for i in range(len(num)):
    if i%2!=0:
        s=s+num[i]
    else:
        s1=s1+num[i]
print(s1-s)