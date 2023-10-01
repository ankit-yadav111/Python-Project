import sys
print("HELLO!, WHAT'S UP!!!.")
print(f"FILE NAME IS {sys.argv[0]}")
print(f"TOTAL NUMBER OF ARGUMENTS = {len(sys.argv)-1}")
print("THE VALUE OF ARGUMENTS: ")
for i in sys.argv:
   print(i)
print("PROGRAM ENDED")
