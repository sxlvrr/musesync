import pandas as pd
import os

data_folder = 'data'
files = ['concerts.csv', 'ecoutes.csv', 'meteo.csv']

for f in files:
    path = os.path.join(data_folder, f)
    df = pd.read_csv(path)
    print(f"Fichier {f} chargé, nombre de lignes (hors header) : {len(df)}")
    print(f"Colonnes: {df.columns.tolist()}")
    print("-" * 30)
