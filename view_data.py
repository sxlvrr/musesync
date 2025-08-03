import psycopg2
import pandas as pd

# Connexion à la base musesync
conn = psycopg2.connect(
    dbname="musesync",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

# Pour exécuter des requêtes
cur = conn.cursor()

# Récupération de toutes les tables de l'utilisateur actuel
cur.execute("""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema='public'
""")
tables = cur.fetchall()
tables = [t[0] for t in tables]

print("📋 Tables disponibles dans la base 'musesync' :")
for t in tables:
    print(f"  - {t}")

print("\n🔍 Aperçu des 10 premières lignes de chaque table :\n")

# Affichage de 10 lignes pour chaque table
for table in tables:
    print(f"🗂️ Table : {table}")
    df = pd.read_sql(f"SELECT * FROM {table} LIMIT 10", conn)
    print(df)
    print("-" * 50)

# Fermeture des connexions
cur.close()
conn.close()
