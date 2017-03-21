from itertools import combinations_with_replacement
s, n = input().split()

n= int(n)
[print(*["".join(i) for i in combinations_with_replacement(sorted(s), n)], sep='\n')]
