
a = map(int,raw_input().split())
b = map(int,raw_input().split())
print ' '.join(map(str,map(sum,zip(*[[x>y,y>x] for x,y in zip(a,b)]))))
