import csv
import pandas as pd
import plotly_express as px
with open('class2.csv',newline='')as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
Total=0
entries= len(fileData)
for marks in fileData:
    Total+=float(marks[1])
mean= Total/entries
print('mean is '+ str(mean))
df = pd.read_csv('class2.csv')
fig=px.scatter(df,x='Student Number',y='Marks')
fig.update_layout(shapes=[
    dict(
        type = 'line',
        y0=mean,
        y1=mean,
        x0=0,
        x1=entries
    )
])
fig.update_yaxes(rangemode='tozero')
fig.show()
