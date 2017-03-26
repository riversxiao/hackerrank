n = int(input())
s = set(map(int, input().split()))
[eval('s.{0}({1})'.format(*input().split()+[''])) for i in range(int(input()))]
print(sum(s))
#this is a harder problem
