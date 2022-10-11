def main(num):
    if num==1:
        return 1
    return num*main(num-1)
x=main(5)
print(x)
