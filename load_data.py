import psycopg2
import pandas as pd
import os

# Config BDD
DB_CONFIG = {
    "dbname": "musesync",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": 5432,
}

# Fichiers à importer
FILES = {
    "artistes": "data/artistes.csv",
    "concerts": "data/concerts.csv",
    "ecoutes": "data/ecoutes.csv",
    "meteo": "data/meteo.csv"
}

def load_csv_to_table(conn, table, filepath):
    print(f"📥 Insertion dans {table} depuis {filepath} ...")
    df = pd.read_csv(filepath)

    # Nettoyage ou ajustements si besoin
    # Ex: remplacer NaN, vérifier types, etc.
    df.fillna('', inplace=True)

    # Création curseur
    cur = conn.cursor()
    try:
        # Suppression des données existantes (optionnel, si tu veux écraser)
        cur.execute(f"DELETE FROM {table};")
        conn.commit()

        # Insertion row by row
        for i, row in df.iterrows():
            cols = ', '.join(row.index)
            vals = ', '.join(['%s'] * len(row))
            sql = f"INSERT INTO {table} ({cols}) VALUES ({vals});"
            cur.execute(sql, tuple(row))
        conn.commit()
        print(f"✅ Table {table} remplie ({len(df)} lignes).")
    except Exception as e:
        print(f"❌ Erreur sur table {table} : {e}")
        conn.rollback()
    finally:
        cur.close()

def main():
    # Connexion
    conn = psycopg2.connect(**DB_CONFIG)
    print("Connexion à la BDD OK")

    for table, filepath in FILES.items():
        if os.path.exists(filepath):
            load_csv_to_table(conn, table, filepath)
        else:
            print(f"⚠️ Fichier {filepath} introuvable, skipping...")

    conn.close()
    print("🎉 Tous les CSV ont été importés avec succès !")

if __name__ == "__main__":
    main()
