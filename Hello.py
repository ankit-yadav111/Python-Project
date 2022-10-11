import sys
print(f"File name is {sys.argv[0]}")
print(f"Total no. of arguments = {len(sys.argv)-1}")
for i in sys.argv:
   print(i)