t=int(input())
while(t>0):
    t-=1
    R1,R2,R3 = input().split()
    V1,V2,V3 = input().split()
    V1=int(V1)
    V2=int(V2)
    V3=int(V3)
    N=int(input())
    D1=V1*N%360
    D2=V2*N%360
    D3=V3*N%360
    if(D1==D2 and D2==D3):
        print("TRUE")
    else:
        print("FALSE")
