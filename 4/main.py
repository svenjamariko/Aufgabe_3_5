import streamlit as st
import numpy as np
import plotly.express as px
from leistungskurve_funktion import read_activity_csv
from leistungskurve_funktion import maxPowerValues
from leistungskurve_funktion import make_powerline_plot


df = read_activity_csv()
df_pc= maxPowerValues(df)
fig = make_powerline_plot(df_pc)
fig.show()
