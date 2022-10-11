'''
a-> ab
b-> cd
c-> cd
d-> ab
'''
n= int(input())
st="a"
b="a"
c=1
while c<n:
    a=b
    b=""
    for i in a:
        if i=="a" or i=="d":
            b+="ab"
        else:
            b+="cd"
        c+=2
    st+=b
print(st[n-1])
