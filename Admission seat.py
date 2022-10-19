import operator
def filterdict(file):
    newfile={}
    for I in file.keys():
        if file[I][3]=="1":
            newfile[I]=file[I][2]
    d = dict( sorted(newfile.items(), key=operator.itemgetter(1)))
    return d
n= int(input())
file={}
s=0
for I in range(n):
    X=input().split()
    s+=int(X[2][0])
    file[I]=X
delfile = filterdict(file)
m=int(input("enter the data"))
for i in range(m):
    x=input().split()
    for j in delfile.keys():
        if int(delfile[j][0])>=int(x[1][0]):
            delfile.pop(j)
            A=0
            for i in range(j):
                A+=int(file[i][2][0])
            print(f"{x[0]} {A}")
            break;
    else:
        print(f"{x[0]} {s}")
        s+=int(x[1][0])
print("executed: ")
