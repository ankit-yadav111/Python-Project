def main(NUM):
    F=1
    for i in range(1,NUM+1):
        F=F*NUM
    return F
x=main(int(input("Enter The Number: ")))
print(x)
