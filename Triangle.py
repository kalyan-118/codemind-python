s1,s2,s3=map(int,input().split())
if s1==s2==s3:
    x="Equilateral triangle"
elif s1==s2 or s2==s3 or s3==s1:
    x="Isosceles triangle"
elif s1!=s2!=s3:
    x="Scalene triangle"
print(x)