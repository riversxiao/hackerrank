print((lambda n,x:(sum(x)/len(x)))(input(),set(map(int,input().split()))))

def average(array):
    return sum(set(arr))/len(set(arr))
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
