if __name__ == '__main__':
    students=[]
    scores =[]
    namelist =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores.append(score)
    slscore=sorted(list(set(scores)))[1]
    [namelist.append(x[0]) for x in students if x[1]==slscore]
    [print (x) for x in sorted(namelist)]
