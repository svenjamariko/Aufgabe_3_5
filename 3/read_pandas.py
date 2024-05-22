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

if __name__ == "__main__":
    df = read_activity_csv()
    print(df.head())
    print(power_mean())
    print(power_max())
    fig = make_power_HR_plot(df)
    fig.show()
    




