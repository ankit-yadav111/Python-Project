dis=int(input())
a,b= input().split()
c,d= input().split()
A= ord(b)-ord(a)+1
N= int(d)-int(c)+1
ans= (A**2)*(N**4)*dis
print(ans)
