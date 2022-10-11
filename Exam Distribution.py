def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

def wrong(n):
    s=1
    for i in range(1,n+1):
        s+=((-1)**i)/fact(i)
    return fact(n)*s

n= int(input())
t=fact(n)
m=int(wrong(n))
print(t-m)
