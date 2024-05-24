# Programmierübung 2 Aufgaben 3-5

# Aufgabe 3: Interaktiver Plot - Leistungstest :chart_with_upwards_trend::chart_with_downwards_trend:
> [!NOTE]
>_Um diese Schritte in VS Code durchzuführen, müssen Sie zunächst sicherstellen, dass Sie Python und VS Code installiert haben._
README.md
# Anleitung zur Verwendung des Codes
**Dieses Repository enthält Code, der entwickelt wurde, um Daten aus einer CSV-Datei zu lesen, sie zu sortieren und sie dann in einem interaktiven Plot darzustellen.**
# Werte im Code

Einige wichtige Werte werden direkt im Code berechnet und definiert. Diese Werte umfassen:

- _Mittelwert der Leistung:_ Der durchschnittliche Leistungswert über den gesamten Zeitraum.
- _Maximalwert der Leistung:_ Der höchste gemessene Leistungswert.
- _Herzfrequenzzonen:_ Fünf definierte Zonen basierend auf der Herzfrequenz.
    - mehr unter: https://www.polar.com/blog/de/effektives-training-mit-herzfrequenz-zonen/

# Werte in Plots

Die Ergebnisse der Analyse werden in Plots dargestellt, die folgende Informationen zeigen:

- _Leistung über die Zeit:_ Ein Linienplot, der die Leistung im Verlauf der Zeit darstellt.
- _Herzfrequenz über die Zeit:_ Ein Linienplot, der die Herzfrequenz im Verlauf der Zeit darstellt.

  
 # Schritte zur Installation und zum Starten der App
1. git clone

2. python -m venv .venv

3. pip install -r requirements.txt

4. streamlit run main.py

5. Streamlit link: http://localhost:8501

<img width="785" alt="image" src="https://github.com/svenjamariko/Aufgabe_3_5/assets/163292776/e5d578e1-0a23-4d53-a56d-c7154da619a3">



:round_pushpin: Die benötigten Bibliotheken für diese App sind in der Datei `requirements.txt` aufgelistet.

# Aufgabe 4: Power Curve

## Übersicht

Dieses Repository enthält ein Python-Skript, das Aktivitätsdaten aus einer CSV-Datei verarbeitet, verschiedene Leistungsmetriken berechnet und die Daten mithilfe von Plotly visualisiert. Das Skript liest die Aktivitätsdaten, berechnet die besten Leistungswerte über verschiedene Zeitintervalle und erstellt Diagramme zur Visualisierung der Leistungsdaten und der Leistungskurve.

## Anforderungen 

- pandas
- numpy
- plotly

Die erforderlichen Bibliotheken können mit pip installiert werden:

```sh
pip install pandas numpy plotly
```

## Beschreibung

Das Skript führt die folgenden Schritte aus:

1. **Aktivitäts-CSV lesen**: Liest eine CSV-Datei mit Aktivitätsdaten und fügt eine Zeitspalte hinzu.
2. **Leistungsdiagramm erstellen**: Erstellt ein Liniendiagramm der Leistungsdaten über die Zeit.
3. **Beste Leistung finden**: Berechnet die maximale gleitende Durchschnittsleistung für angegebene Zeitintervalle.
4. **Maximale Leistungswerte**: Berechnet die besten Leistungswerte für bestimmte Intervalle und erstellt ein DataFrame.
5. **Leistungskurvendiagramm erstellen**: Erstellt ein Leistungskurvendiagramm, das die besten Leistungswerte für verschiedene Intervalle zeigt.

### Funktionen

#### `read_activity_csv()`
Liest die CSV-Datei ein und gibt ein DataFrame mit den Aktivitätsdaten zurück. Die Funktion fügt auch eine `time`-Spalte hinzu, die die verstrichene Zeit darstellt.

#### `make_power_plot(df)`
Nimmt ein DataFrame `df` und erstellt ein Liniendiagramm der ursprünglichen Leistungsdaten mithilfe von Plotly.

#### `find_best_effort(df, time, f_s)`
Berechnet die maximale Durchschnittsleistung über ein angegebenes Zeitintervall `time` mit einer Abtastfrequenz `f_s`. Gibt den maximalen Leistungswert zurück.

#### `maxPowerValues(df)`
Berechnet die besten Leistungswerte für die Intervalle 1s, 30s, 60s, 300s, 600s und 1200s. Gibt ein DataFrame mit diesen Leistungswerten und den entsprechenden Intervallen zurück.

#### `make_powerline_plot(df_pc)`
Nimmt ein DataFrame `df_pc`, das die Leistungswerte für verschiedene Intervalle enthält, und erstellt mithilfe von Plotly ein Leistungskurvendiagramm.

## Anwendung

1. **CSV-Datei vorbereiten**: Stellen Sie sicher, dass die CSV-Datei `activity.csv` im richtigen Verzeichnis abgelegt ist. Die CSV sollte eine Spalte `Duration` und eine Spalte `PowerOriginal` enthalten.
2. **Skript ausführen**: Führen Sie das Skript mit Python aus:

   ```sh
   python main.py
   ```

3. **Diagramme anzeigen**: Das Skript erzeugt und zeigt das Leistungskurvendiagramm mithilfe von Plotly an.

![image](https://github.com/svenjamariko/Aufgabe_3_5/assets/163292776/51ad39d4-3da2-42d8-ba08-acf747962659)

