import streamlit as st
import read_person_data
import ekgdata
import matplotlib.pyplot as plt
from PIL import Image

def callback():
    print(f"The user has changed to{st.session_state.aktuelle_versuchsperson} and {st.session_state.aktuelles_ekg}")

# Zu Beginn

# Lade alle Personen
person_names = read_person_data.get_person_list(read_person_data.load_person_data())

# Anlegen diverser Session States
## Gewählte Versuchsperson
if 'aktuelle_versuchsperson' not in st.session_state:
    st.session_state.aktuelle_versuchsperson = 'None'

## Anlegen des Session State. Bild, wenn es kein Bild gibt
if 'picture_path' not in st.session_state:
    st.session_state.picture_path = 'data/pictures/none.jpg'

## Session State für Pfad zu EKG Daten 
if 'ekg_path' not in st.session_state:
    st.session_state.ekg_path = ''

# Design des Dashboards

# Schreibe die Überschrift
st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Auswahlbox, wenn Personen anzulegen sind
st.session_state.aktuelle_versuchsperson = st.selectbox(
    'Versuchsperson',
    options = person_names, key="select_versuchsperson")

# Name der Versuchsperson
st.write("Der Name ist: ", st.session_state.aktuelle_versuchsperson)

# Date input slot
current_person_dict = read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)

ekg_data = current_person_dict["ekg_tests"]
ekg_datum = [ekg["date"] for ekg in ekg_data]

st.write("## Datum auswählen")
st.session_state.aktuelles_ekg = st.selectbox(
    'EKG-Datum',
    options = ekg_datum, key="sbEKGDatum",
    on_change=callback)
ekg_data = [ekg for ekg in ekg_data if ekg["date"] == st.session_state.aktuelles_ekg][0]


st.write("Das ausgewählte Datum ist:", ekg_data)

# TODO: Weitere Daten wie Geburtsdatum etc. schön anzeigen

# Nachdem eine Versuchsperson ausgewählt wurde, die auch in der Datenbank ist
# Finde den Pfad zur Bilddatei
if st.session_state.aktuelle_versuchsperson in person_names:
    person_data = read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)
    st.session_state.picture_path = person_data.get("picture_path", 'data/pictures/none.jpg')
    st.session_state.ekg_path = person_data.get("ekg_path", '')  # Use .get to handle missing keys

# Bild anzeigen
image = Image.open(st.session_state.picture_path)
st.image(image, caption=st.session_state.aktuelle_versuchsperson)

# Öffne EKG-Daten
# TODO: Für eine Person gibt es ggf. mehrere EKG-Daten. Diese müssen über den Pfad ausgewählt werden können
# Vergleiche Bild und Person
if st.session_state.ekg_path:
    current_ekg_data = ekgdata.EKGdata(st.session_state.ekg_path)

    # EKG-Daten als Matplotlib Plot anzeigen
    # Nachdem die EKG, Daten geladen wurden
    # Erstelle den Plot als Attribut des Objektes
    current_ekg_data.plot_time_series()
    # Zeige den Plot an
    st.pyplot(fig=current_ekg_data.fig)

    # Herzrate bestimmen
    # Schätze die Herzrate 
    current_ekg_data.estimate_hr()
    # Zeige die Herzrate an
    st.write("Herzrate ist: ", int(current_ekg_data.heat_rate))
else:
    st.write("Keine EKG-Daten vorhanden.")