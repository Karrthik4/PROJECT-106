import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
        fig.show()
        
def getDataSource(data_path):
    Sleep_Hours = []
    Coffee_Cups = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Sleep_Hours.append(float(row["sleep in hours"]))
            Coffee_Cups.append(float(row["Coffee in ml"]))
    return{"x":Sleep_Hours, "y":Coffee_Cups}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between Cups of coffe and hours of sleep", correlation[0,1])

def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)
    
setup()