from collections import Counter
n =int(input())
items=list(map(int,input().split()))
print (sum(items)/n)
items=sorted(items)
if n%2 ==1:
    print(items[n//2])
else:
    print((items[n//2-1]+items[n//2])/2)
import operator
x_items =sorted(Counter(items).items(),key=operator.itemgetter(1), reverse=True)

print (min([x[0] for x in x_items if x[1]==Counter(items).most_common(1)[0][1]]))

################################
#Do not reinvent the wheel
import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))
