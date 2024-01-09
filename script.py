import os
import mysql.connector
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer les informations de connexion à partir des variables d'environnement
db_host = os.getenv("DB_HOST")
db_user = os.getenv("root")
db_password = os.getenv("")
db_database = os.getenv("bibliothèque musical")

# Établir la connexion à la base de données
connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database
)

# Utiliser la connexion pour effectuer des opérations sur la base de données
cursor = connection.cursor()

# Exemple : récupérer toutes les tables de la base de données
cursor.execute("SHOW TABLES")

tables = cursor.fetchall()

for table in tables:
    print(table)

# Fermer la connexion
cursor.close()
connection.close()

