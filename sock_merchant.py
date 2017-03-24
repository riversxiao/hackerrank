import sys

from collections import Counter

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

stocks = Counter(c)
new=list(stocks.items())
print (sum([x[1]//2 for x in new]))
