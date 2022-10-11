import operator
def filterdict(file):
    newfile={}
    for i in file.keys():
        if file[i][3]=="1":
            newfile[i]=file[i][2]
    d = dict( sorted(newfile.items(), key=operator.itemgetter(1)))
    return d
n= int(input())
file={}
s=0
for i in range(n):
    x=input().split()
    s+=int(x[2][0])
    file[i]=x
delfile = filterdict(file)
m=int(input())
for i in range(m):
    x=input().split()
    for j in delfile.keys():
        if int(delfile[j][0])>=int(x[1][0]):
            delfile.pop(j)
            a=0
            for i in range(j):
                a+=int(file[i][2][0])
            print(f"{x[0]} {a}")
            break;
    else:
        print(f"{x[0]} {s}")
        s+=int(x[1][0])
