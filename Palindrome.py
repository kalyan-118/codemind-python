a=int(input())
b=a
c=0
while(a>0):
    d=a%10
    c=c*10+d
    a=a//10
if b==c:
    print("True")
else:
    print("False")