f = open(r"C:\Users\wenxiao\Desktop\test\difference1.csv", 'wt')
try:
    writer = csv.writer(f)

    writer.writerow(finalresult1)
finally:
    f.close()

union =secondone.union(firstone)
path = r"C:\Users\wenxiao\Desktop\test\spoofcase1.csv"
import csv
with open(path) as f:
    reader = csv.reader(f)
    data =[]
    for row in reader:
        for a in row:
            data.append(a)
