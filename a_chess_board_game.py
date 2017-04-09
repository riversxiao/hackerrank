t = int(input())
for _ in range(t):

    x,y = map(int, input().split())
    print(["Second","First"][(y%4 ==0 or y%4 == 3) or (x%4==0 or x%4==3)])
