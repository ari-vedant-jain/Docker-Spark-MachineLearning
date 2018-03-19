#!/user/bin/python
import urllib2
import json
import csv
data = '{"x": -9.118195, "y": -3.537857, "z": -0.89404297, "User": "c", "Model": "lgwatch", "Device": "lgwatch_2"}'
url = 'http://localhost:15000'

def get_prediction(url, data):
    r = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    response = urllib2.urlopen(r)
    f = json.loads( response.read())
    response.close()
    return f

x = get_prediction(url, data)
d = int(x["prediction"])
d = str(d)
print d
with open('export.csv', 'rb') as index:
    reader = csv.reader(index, delimiter=",")
    next(reader, None)
    gt = [row[0] for row in reader if row[1] == d]
    gt = "".join(str(x) for x in gt)
    print "{prediction: '%s'}" % gt




	

