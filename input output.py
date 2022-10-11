def main(num):
    f=1
    for i in range(1,num+1):
        f=f*num
    return f
x=main(int(input("Enter the Number: ")))
print(x)
