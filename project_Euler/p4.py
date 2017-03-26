def maxn(targets):
    n=0
    for a in range(999, 100, -1):
        for b in range(min(999,int(targets/a)), 100, -1):
            x = a * b
            if x > n:
                s = str(a * b)
                if s == s[::-1] and a*b<targets:

                    n =a * b
    print (n)

n = int(input())
for _ in range(n):
    maxn(int(input()))
