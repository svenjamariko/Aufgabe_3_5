import streamlit as st
from read_pandas import read_my_csv
from read_pandas import make_plot
from read_pandas import read_activity_csv
from read_pandas import make_power_HR_plot
from read_pandas import calculate_zones
from read_pandas import calculate_time_in_zones
from read_pandas import calculate_avg_power_in_zones
import plotly.express as px

if 'max_hr' not in st.session_state:
    st.session_state.max_hr = 180

# Wo startet sie Zeitreihe
# Wo endet sich
# Was ist die Maximale und Minimale Spannung
# Grafik
tab1, tab2 = st.tabs(["EKG-Data", "Power-Data"])

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

    df = read_my_csv()
    fig = make_plot(df)

    st.plotly_chart(fig)

with tab2:
    st.header("Power-Data")
    st.write("# My Plot")
    df = read_activity_csv()
    fig = make_power_HR_plot(df)
    st.session_state.max_hr = st.number_input('Gib die maximale Herzfrequenz ein', min_value=100, max_value=220, value=180)

    
    st.plotly_chart(fig)

    # Berechne Zonen
    st.title("Herzfrequenz Zonen Berechnung")
    df = calculate_zones(df, st.session_state.max_hr)

    # Zeige Zonen an
    st.write("Zeit in den Zonen:")
    time_in_zones = calculate_time_in_zones(df)
    st.write(f"Zone 1: {time_in_zones[0]} Sekunden")
    st.write(f"Zone 2: {time_in_zones[1]} Sekunden")
    st.write(f"Zone 3: {time_in_zones[2]} Sekunden")
    st.write(f"Zone 4: {time_in_zones[3]} Sekunden")
    st.write(f"Zone 5: {time_in_zones[4]} Sekunden")

    # Zeige durchschnittliche Leistung in den Zonen an
    st.write("Durchschnittliche Leistung in den Zonen:")
    avg_power_in_zones = calculate_avg_power_in_zones(df)
    st.write(f"Zone 1: {avg_power_in_zones[0]} Watt")
    st.write(f"Zone 2: {avg_power_in_zones[1]} Watt")
    st.write(f"Zone 3: {avg_power_in_zones[2]} Watt")
    st.write(f"Zone 4: {avg_power_in_zones[3]} Watt")
    st.write(f"Zone 5: {avg_power_in_zones[4]} Watt")
