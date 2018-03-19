import csv

with open('export.csv', 'rb') as index:
    d = 3
    d = str(d)
    print type(d)
    reader = csv.reader(index, delimiter=",")
    next(reader, None)
    gt = [row[0] for row in reader if row[1] == d]
gt = "".join(str(x) for x in gt)
print "{prediction: '%s'}" % gt
