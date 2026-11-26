# HÄMTA: hämtar data från Eurostat.
import eurostat


def hamta_data(kod, filter_val):
    # Svaret blir en bred tabell: en rad per land och en kolumn per år.
    return eurostat.get_data_df(kod, filter_pars={**filter_val, "startPeriod": 2000})
