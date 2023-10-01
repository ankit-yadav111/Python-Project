N=int(input())
list2=[]
for i in range(N):
    s=input()
    list2.append(s)
stud=input().split(",")
sl=len(stud)
mid= sl//2
i=mid
s=[]
while i!=sl:
    s.append(int(stud[i]))
    i+=1
for i in range(mid-1,-1,-1):
    s.append(int(stud[i]))
row=[]
for i in range(n):
    c=0
    for j in list2[i]:
        if j=="_":
            c+=1
    row.append(c)
ans=[]
i=0
while i<n:
    i+=1
    ans.append("")
i=0
while i<s1:
    for j in range(n):
        if s[i]<=row[j]:
            row[j]-=s[i]
            res=ans[j]
            count=0
            k=len(res)
            while k!=len(list2[j]) and count!=s[i]:
                if list2[j][k]=="_":
                    res+=str(i+1)
                    count+=1
                if list2[j][k]=="X":
                    res+="X"
                k+=1
            ans[j]=res
            break
    i+=1
for i in range(n):
    a=list2[i]
    l=len(ans[i])
    l1=len(a)
    if l<l1:
        res=ans[i]+a[l:]
        ans[i]=res
for i in ans:
    print(i)
