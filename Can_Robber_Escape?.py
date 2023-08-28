r=int(input())
v=list(map(int,input().split()))
l=0
for k in v:
    if k%2!=0:
        l+=1
if l<=2:
    print("YES")
else:
    print("NO")
