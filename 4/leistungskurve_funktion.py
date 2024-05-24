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
    rolling_power = df["PowerOriginal"].rolling(window=int(time*f_s)).mean() 
    max_power = rolling_power.max()
    return max_power # max power in the frame: time seconds, f_s Hz

def maxPowerValues(df):
    PowerValues = []
    PowerValues.append(find_best_effort(df, 1, 1))
    PowerValues.append(find_best_effort(df, 30, 1))
    PowerValues.append(find_best_effort(df, 60, 1))
    PowerValues.append(find_best_effort(df, 300, 1))
    PowerValues.append(find_best_effort(df, 600, 1))
    PowerValues.append(find_best_effort(df, 1200, 1))
    #print(PowerValues)
    time = [1, 30, 60, 300, 600, 1200]
    PowerValuesD ={"Interval in s": time, "Power Values in W": PowerValues}
    df_pc = pd.DataFrame(PowerValuesD)
    print(df_pc)
    return df_pc

def make_powerline_plot(df_pc):
    
    fig = px.line(df_pc, x="Interval in s", y='Power Values in W' )
    fig.update_layout(title = "Power Curve")
    return fig


if __name__ == "__main__":
    df = read_activity_csv()
    df_pc= maxPowerValues(df)
    fig = make_powerline_plot(df_pc)
    fig.show()
    

