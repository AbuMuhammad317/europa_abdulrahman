# Anslutningen till databasen.
# Lösenordet står i filen .env och inte här i koden.
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()                                   # läser .env
engine = create_engine(os.getenv("DB_URL"))     # används för att prata med databasen

# Körs bara när man skriver "python db.py". Då testas anslutningen.
if __name__ == "__main__":
    try:
        with engine.connect() as anslutning:
            version = anslutning.execute(text("SELECT VERSION()")).scalar()
        print("Anslutningen fungerar. Databasserver:", version)
    except Exception as fel:
        # Skriv bara typen av fel, så att inga inloggningsuppgifter visas.
        print("Det gick inte att ansluta:", type(fel).__name__)
