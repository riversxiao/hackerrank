import math
n = int(input())
numbers = list(map(int, input().split()))
exp= sum(numbers)/n
variance =sum([(x-exp)**2 for x in numbers])/n
std = math.sqrt(variance)
print (round(std,1))
