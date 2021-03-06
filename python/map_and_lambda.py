fib = lambda y: y if y < 2 else fib(y - 1) + fib(y - 2)
print map(lambda x: x**3, map(fib, range(input())))

###
cube = lambda x: x**3# complete the lambda function
def fibonacci(n):
    # return a list of fibonacci numbers
    lis = [0,1]
    for i in range(2,n):
        lis.append(lis[i-2] + lis[i-1])
    return(lis[0:n])
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
###
memo = {0:0, 1:1}
def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]
