import csv
import math
with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    fileData=list(reader)
data =fileData[0]
print(data)
def mean(data):
    n = len(data)
    Total = 0
    for x in data:
        Total+= int(x)
    mean = Total/n
    return mean
list=[]
for x in data:
    a = int(x)-mean(data)
    a = a**2
    list.append(a)
# claculate sumt
sum = 0 
for i in list:
    sum = sum + i
# divideing 
result =float(sum)/(len(data)-1)
# get the devation
stddev = math.sqrt(result)
print(stddev)