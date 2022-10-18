import sys
print("HELLO!, HOW ARE YOU...")
print(f"FILE NAME IS {sys.argv[0]}")
print(f"TOTAL NUMBER OF ARGUMENTS = {len(sys.argv)-1}")
print("The VALUE OF ARGUMENTS: ")
for i in sys.argv:
   print(i)
print("Program Ended")
