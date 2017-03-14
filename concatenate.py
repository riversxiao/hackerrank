import numpy as np
N, M, _ = [int(x) for x in input().strip().split()]
a, b = map(lambda x: np.array([input().strip().split() for i in range(int(x))], int), [N, M])
print (np.concatenate((a, b), axis = 0))


t = int(input())
for _ in range(2*t):
    piles = int(input())
    pilec = map(int, input().split())
    zeros = sum([x==0 for x in pilec])
    newpile = piles-zeros
    if newpile % 2 ==0 :
        print ("Second")
    else:
        print ("First")
    
