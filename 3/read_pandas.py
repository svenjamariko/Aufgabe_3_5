# Paket für Bearbeitung von Tabellen
import pandas as pd
import numpy as np

# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
import plotly.express as px


def read_my_csv():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv("data/ekg_data/01_Ruhe.txt", sep="\t", header=None)

    # Setzt die Columnnames im Dataframe
    df.columns = ["Messwerte in mV","Zeit in ms"]
    
    # Gibt den geladen Dataframe zurück
    return df


def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x= "Zeit in ms", y="Messwerte in mV")
    return fig


def read_activity_csv():
    df = pd.read_csv("data/activities/activity.csv", sep=",")
    n = df["Duration"].sum()
    df["time"]= np.arange(0,n)
    return df

def power_mean():
    p_mean = df["PowerOriginal"].mean()
    return p_mean
    
def power_max():
    p_max = df["PowerOriginal"].max()
    return p_max

def make_power_HR_plot(df):
    fig = px.line(df, x="time", y=['PowerOriginal', 'HeartRate'] )
    return fig

def calculate_max_hr(df):
    max_hr = df['HeartRate'].max()
    return max_hr

def calculate_mean_hr(df):          
    mean_hr = df['HeartRate'].mean()
    return mean_hr

def calculate_zones(df, max_hr):
    zone_1_min = 0.5 * max_hr
    zone_1_max = 0.6 * max_hr
    zone_2_max = 0.7 * max_hr
    zone_3_max = 0.8 * max_hr
    zone_4_max = 0.9 * max_hr
    zone_5_max = 1 * max_hr

    df['zone 1'] = (df['HeartRate'] >= zone_1_min) & (df['HeartRate'] < zone_1_max)
    df['zone 2'] = (df['HeartRate'] >= zone_1_max) & (df['HeartRate'] < zone_2_max)
    df['zone 3'] = (df['HeartRate'] >= zone_2_max) & (df['HeartRate'] < zone_3_max)
    df['zone 4'] = (df['HeartRate'] >= zone_3_max) & (df['HeartRate'] < zone_4_max)
    df['zone 5'] = (df['HeartRate'] >= zone_4_max) & (df['HeartRate'] < zone_5_max)


    return df

if __name__ == "__main__":
    df = read_activity_csv()
    print(df.head())
    print(power_mean())
    print(power_max())
    fig = make_power_HR_plot(df)
    fig.show()
    max_hr = calculate_max_hr(df)
    mean_hr = calculate_mean_hr(df)
    zones = calculate_zones(df, max_hr)
    print(max_hr, mean_hr, zones)
    df = calculate_zones(df,max_hr)
    print(df["zone 1"])
    




