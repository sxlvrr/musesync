import pandas as pd
import random
from datetime import datetime, timedelta

# Paramètres
genres = ["Hip-Hop", "Indie Pop", "Electro", "Rock", "Jazz", "Techno", "Folk", "World", "Trap", "Ambient"]
lieux = ["La Vapeur", "Le Rocher", "L’Escale", "Underground Club", "Nova Scene", "L'Oasis", "Echo Hall"]
plateformes = ["Spotify", "Deezer", "YouTube Music", "Apple Music"]

n_artistes = 30
n_concerts = 300
n_ecoutes = 5000
n_jours_meteo = 120

# ARTISTES
artistes = []
for i in range(n_artistes):
    nom = f"Artiste_{i+1}"
    genre = random.choice(genres)
    bpm = random.randint(75, 140)
    energie = round(random.uniform(0.3, 0.95), 2)
    popularite = random.randint(20, 95)
    artistes.append({"id": i+1, "nom": nom, "genre": genre, "bpm": bpm, "energie": energie, "popularite": popularite})

df_artistes = pd.DataFrame([[
    a["id"], a["nom"], a["genre"], a["bpm"], a["energie"], a["popularite"]
] for a in artistes], columns=["id", "nom", "genre", "bpm_moyen", "energie", "popularite"])
df_artistes.to_csv("artistes.csv", index=False)

# CONCERTS
concerts = []
for i in range(1, n_concerts + 1):
    a = random.choice(artistes)
    date = datetime(2024, 6, 1) + timedelta(days=random.randint(0, 120))
    lieu = random.choice(lieux)
    meteo = random.choice(["Ensoleille", "Pluvieux", "Nuageux", "Orage", "Canicule", "Brume"])
    prix = random.choice([8, 10, 12, 15, 18, 20])
    nb_vendus = random.randint(30, 500)
    concerts.append([i, a["id"], lieu, date.date(), meteo, prix, nb_vendus])

df_concerts = pd.DataFrame(concerts, columns=[
    "id", "id_artiste", "lieu", "date", "meteo", "prix", "nb_tickets_vendus"
])
df_concerts.to_csv("concerts.csv", index=False)

# ECOUTES
ecoutes = []
for i in range(1, n_ecoutes + 1):
    a = random.choice(artistes)
    date = datetime(2024, 6, 1) + timedelta(days=random.randint(0, 120))
    nb = random.randint(200, 15000)
    plateforme = random.choice(plateformes)
    ecoutes.append([i, a["id"], date.date(), nb, plateforme])

df_ecoutes = pd.DataFrame(ecoutes, columns=[
    "id", "id_artiste", "date", "nombre_ecoutes", "plateforme"
])
df_ecoutes.to_csv("ecoutes.csv", index=False)

# METEO
meteo_data = []
for i in range(n_jours_meteo):
    date = datetime(2024, 6, 1) + timedelta(days=i)
    for lieu in lieux:
        temp = random.randint(10, 35)
        condition = random.choice(["Ensoleille", "Pluvieux", "Nuageux", "Orage", "Canicule", "Brume"])
        meteo_data.append([lieu, date.date(), temp, condition])

df_meteo = pd.DataFrame(meteo_data, columns=[
    "lieu", "date", "temperature", "meteo"
])
df_meteo.to_csv("meteo.csv", index=False)

print("🚀 CSV réalistes générés avec succès dans le dossier /data !")
