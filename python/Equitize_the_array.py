from collections import Counter
number = int(input())
items= Counter(list(map(int,input().split())))
print(number - items.most_common(1)[0][1])
