n,k =map(int,input().split())
items =list(map(int, input().split()))
bill = int(input())
del items[k]
[print("Bon Appetit") if bill-sum(items)/2==0 else print(int(bill-sum(items)/2))]
