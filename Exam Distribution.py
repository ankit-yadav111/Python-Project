def fact(N):
    F=1
    for i in range(1,N+1):
        F*=i
    return F

def wrong(N):
    S=1
    I=1
    while I<N+1:
        S+=((-1)**I)/fact(I)
        I=I+1
    return fact(N)*S

n= int(input("Enter The Value Of N: "))
t=fact(n)
m=int(wrong(n))
print(t-m)
print("Program Ended: ")
