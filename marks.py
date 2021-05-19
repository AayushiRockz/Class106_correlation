import pandas as pd 
import plotly.express as px
import numpy as np
import csv

with open("marks.csv",newline='') as f:
    df = pd.read_csv(f)
    fig = px.scatter(df, x="Days Present",y="Marks In Percentage")
    fig.show()

def getDataSource(data_path):
    marks=[]
    daysPresent=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    return{"x":daysPresent,"y":marks}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation:" ,correlation[0,1])

def main():
    data_path = "marks.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

main()


