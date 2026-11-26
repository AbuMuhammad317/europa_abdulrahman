# RENSA: gör tabellen lätt att läsa.


def rensa_data(bred):
    # Byt namn på landkolumnen.
    bred = bred.rename(columns={"geo\\TIME_PERIOD": "land"})

    # Gör om från en kolumn per år till en rad per land och år.
    ar_kolumner = [k for k in bred.columns if k.isdigit()]
    lang = bred.melt(id_vars="land", value_vars=ar_kolumner, var_name="ar", value_name="varde")
    lang["ar"] = lang["ar"].astype(int)

    # Tomma värden tas inte bort.
    return lang
