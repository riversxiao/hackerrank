#medium hard
N,M = map(int, input().split())
data  = [input() for _ in range(N)]
K=int(input())
for row in sorted(data, key=lambda row: int(row.split()[K])):
    print(row)
 
