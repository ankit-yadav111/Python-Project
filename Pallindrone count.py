def palindrome(st):
    st_rev=st[::-1]
    if st_rev==st:
        return 1
    return 0

n=int(input("Enter The Value Of N: "))
st=input("Enter The String: ")
m=int(input("Enter The Value Of M: "))
m_list = input("Enter The Value Of List Element: ").split()
count=0
for i in m_list:
    i=int(i)
    for j in range(n-i+1):
        if palindrome(st[j:i+j:1]):
            count+=1
print(count)
print("Program Ended:")
