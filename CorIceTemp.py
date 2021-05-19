from numpy import DataSource, corrcoef
import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    temperature= []
    iceCream_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            temperature.append(float(row["Temperature"]))
            iceCream_sales.append(float(row["Ice-cream Sales( â‚¹ )"]))
    return {"x": temperature, "y":iceCream_sales}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("correlation between temperature and ice-cream sales is: ", correlation[0,1] )

def setup():
    data_path = "IceTemp.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
    