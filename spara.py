# SPARA: lägger in tabellen i databasen.
from db import engine


def spara_data(tabell, namn):
    # Finns tabellen redan så ersätts den. Tomma värden blir NULL.
    tabell.to_sql(namn, engine, if_exists="replace", index=False)
    print(f"{namn}: {len(tabell)} rader, varav {tabell['varde'].isna().sum()} utan värde")
