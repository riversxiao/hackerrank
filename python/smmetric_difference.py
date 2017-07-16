t = input()
m= set(map(int, input().split()))
t = input()
n= set(map(int, input().split()))

lis= n.difference(m).union(m.difference(n))
lis = sorted(list(lis))

[print(x) for x in lis]
# sorted() works fine, but sort() won't work

a,b = [set(raw_input().split()) for _ in range(4)][1::2]
print '\n'.join(sorted(a^b, key=int))
