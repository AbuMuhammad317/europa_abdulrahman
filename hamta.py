# Hämtar data från Eurostat och sparar den i databasen.
import eurostat

from db import engine


def hamta_och_spara(kod, filter_val, tabell):
    # 1. Hämta från Eurostat från år 2000. Svaret blir en tabell (DataFrame).
    data = eurostat.get_data_df(kod, filter_pars={**filter_val, "startPeriod": 2000})

    # 2. Gör om från bred tabell (en kolumn per år) till lång (en rad per land och år).
    data = data.rename(columns={"geo\\TIME_PERIOD": "land"})
    ar_kolumner = [k for k in data.columns if k.isdigit()]
    lang = data.melt(id_vars="land", value_vars=ar_kolumner, var_name="ar", value_name="varde")
    lang["ar"] = lang["ar"].astype(int)

    # 3. Spara i databasen. Tomma värden blir NULL.
    lang.to_sql(tabell, engine, if_exists="replace", index=False)
    print(f"{tabell}: {len(lang)} rader, varav {lang['varde'].isna().sum()} utan värde")


# Arbetslöshet i procent av arbetskraften, 25-74 år, båda könen.
hamta_och_spara("une_rt_a", {"sex": ["T"], "age": ["Y25-74"], "unit": ["PC_ACT"]}, "arbetsloshet")
