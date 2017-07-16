if __name__ == '__main__':
    n = int(input())
    result = []
    for _ in range(n):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("result."+cmd)
        else:
            print (result)
