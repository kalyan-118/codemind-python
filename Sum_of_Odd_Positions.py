n=int(input())
num=list(map(int,input().split()))
s=0
for i in range(0,len(num)):
    if i%2!=0:
        s+=num[i]
print(s)