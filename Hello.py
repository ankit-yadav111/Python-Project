import sys
print("Hello!, How are you...")
print(f"File name is {sys.argv[0]}")
print(f"Total no. of arguments = {len(sys.argv)-1}")
print("The value of Arguments are: ")
for i in sys.argv:
   print(i)
print("Program Ended")
