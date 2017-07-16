import sys
N = int(input().strip())
print (["Weird","Not Weird"][N%2 == 0 and (N in range(2,6) or N > 20)])  
