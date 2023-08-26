n=int(input())
if n<=10000:
    da=int((80/100)*n)
    hra=int((20/100)*n)
    gs=int(n+da+hra)
elif n<=20000:
    da=int((90/100)*n)
    hra=int((25/100)*n)
    gs=int(n+da+hra)
else:
    da=int((95/100)*n)
    hra=int((30/100)*n)
    gs=int(n+da+hra)
print(f'{gs:.2f}')