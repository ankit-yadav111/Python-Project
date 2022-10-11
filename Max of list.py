'''list1=input("Enter the List Element:").split()
k=int(input("Enter the Search Key: "))
for i in range(len(list1)):
    if int(list1[i])==k:
        print("Element index is : ",i)
        break
else:
    print(f"{k} is not in the  List: ")
    

'''
list1=input("Enter the List Element:").split()
max=int(list1[0])
for i in list1[1:]:
    if int(i)>max:
        max=int(i)
print("Maximum Element is ",max)
 
