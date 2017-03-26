n = int(input())
t =list(map(int, input().split()))
if all([i>0 for i in t]):
    print (any([str(i)==str(i)[::-1] for i in t]))
else:
    print (False)
