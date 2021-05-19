import csv
import plotly.express as px
import pandas as pd

with open("tvHours.csv",newline='') as csv_file:
    df = pd.read_csv(csv_file)
    fig = px.scatter(df,x = "Size of TV", y="\tAverage time spent watching TV in a week (hours)")
    fig.show()



