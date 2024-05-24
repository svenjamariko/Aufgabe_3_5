import pandas as pd
import numpy as np
import plotly.express as px

def read_activity_csv():
    df = pd.read_csv("data/activities/activity.csv", sep=",") # read the csv file
    n = df["Duration"].sum()
    df["time"]= np.arange(0,n) # create a new column with the time
    return df

def make_power_plot(df):
    fig = px.line(df, x="time", y=['PowerOriginal'] )
    return fig 

def find_best_effort(df, time, f_s):
    df["PowerOriginal"] = df["PowerOriginal"].rolling(window=int(time*f_s)).mean() 
    max_power = df["PowerOriginal"].max()
    return max_power
 
   

if __name__ == "__main__":
    df = read_activity_csv()
    fig = make_power_plot(df)
    #fig.show()
    print(find_best_effort(df, 10, 1)) # 10 seconds, 1 Hz