import sys
from collections import Counter
n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
# your code goes here
print(Counter(types).most_common(1)[0][0])
