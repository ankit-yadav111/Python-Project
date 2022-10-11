def palindrome(st):
    st_rev=st[::-1]
    if st_rev==st:
        return 1
    return 0

n=int(input("Enter the value of N: "))
st=input("Enter the String: ")
m=int(input("Enter the value of M: "))
m_list = input("Enter the value of List Element: ").split()
count=0
for i in m_list:
    i=int(i)
    for j in range(n-i+1):
        if palindrome(st[j:i+j:1]):
            count+=1
print(count)
print("Program Ended:")
