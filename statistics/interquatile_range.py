def median(nums):
    if len(nums)%2 == 0:
        return int(sum(nums[len(nums)//2-1:len(nums)//2+1])/2)
    else:
        return nums[len(nums)//2]

def quartiles(N,nums):
    Q1 = median(nums[:len(nums)//2])
    Q2 = median(nums)
    if N%2 == 0:
        Q3 = median(nums[len(nums)//2:])
    else:
        Q3 = median(nums[len(nums)//2+1:])
    return Q1,Q2,Q3
from collections import Counter
n=input()
elem = list(map(int,input().split()))
count = list(map(int, input().split()))
t = sorted(list(Counter(dict(zip(elem,count))).elements()))

N =len(t)
Q1,Q2,Q3 = quartiles(N,t)
print (round(float(Q3-Q1),1))
