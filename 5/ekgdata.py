import json
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

## Konstruktor der Klasse soll die Daten einlesen

    def __init__(self, ekg_dict):
        pass
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['EKG in mV','Time in ms',])
        #self.peaks = self.find_peaks()


    def load_by_id(ekg_id):
        file = open("data/person_db.json")
        person_data = json.load(file)

        for person in person_data:
            ekg_tests = person['ekg_tests']
            for ekg in ekg_tests:
                if ekg["id"] == ekg_id:
                    return ekg
            return None
        

    def find_peaks(series, threshold, respacing_factor=5):
    
    # Respace the series
        series = series.iloc[::respacing_factor]
    
    # Filter the series
        series = series[series>threshold]


        peaks = []
        last = 0
        current = 0
        next = 0

        for index, row in series.items():
            last = current
            current = next
            next = row

            if last < current and current > next and current > threshold:
                peaks.append(index-respacing_factor)

        return peaks
        
    def estimate_hr(peaks):
        peak_times_sec = np.array(peaks) / 1000
        rr_intervals = np.diff(peak_times_sec)
        heart_rate_at_peaks = 60 / rr_intervals
        heart_rate_times = peak_times_sec[1:]
        return heart_rate_times, heart_rate_at_peaks, peak_times_sec

    def make_ekg_plot(peak_times_sec, df):
        fig = px.line(df, x="Time in s", y=['EKG in mV'])
        fig.add_trace(go.Scatter(x=df["Time in ms"].iloc[peaks], y=df["EKG in mV"].iloc[peaks], mode='markers', name='Peaks'))
        return fig
# %% Testen der Funktionen

if __name__ == "__main__":
    #print("This is a module with some functions to read the EKG data")
    file = open("data/person_db.json")
    person_data = json.load(file)
    #print(person_data)
    ekg_dict = person_data[0]["ekg_tests"][0]
    #print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    #print(ekg.df.head())
    Ekg_1 = EKGdata.load_by_id(1)
    #print(Ekg_1)
    df = pd.read_csv(r'data/ekg_data/01_Ruhe.txt', sep='\t', header=None, names=['EKG in mV','Time in ms',])
    peaks = EKGdata.find_peaks(df["EKG in mV"].copy(), 340, 5)
    #print(peaks)
    heart_rate_times, heart_rate_at_peaks, peak_time_sec = EKGdata.estimate_hr(peaks)
    #print(heart_rate_times)
    #print(heart_rate_at_peaks)
    fig = EKGdata.make_ekg_plot(peak_time_sec, df)
    fig.show()


