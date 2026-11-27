# Glider Europa isär?

Ett projekt i kursen Avancerad Analys på YH Borås. Jag hämtar data från Eurostat, sparar den
i en databas och analyserar den.

## Frågorna

1. Var i Europa (EU) är det svårast att få jobb i dag?
2. Har länder med välutbildad befolkning lägre arbetslöshet?

## Flödet

```
Eurostat -> hamta.py -> rensa.py -> spara.py -> databasen -> analys.ipynb
```

`kor.py` kör de tre första stegen i ordning.

## Filerna

| Fil | Vad den gör |
|---|---|
| `kor.py` | Kör hämta, rensa och spara |
| `hamta.py` | Hämtar data från Eurostat |
| `rensa.py` | Gör tabellen lång: en rad per land och år |
| `spara.py` | Sparar tabellen i databasen |
| `db.py` | Anslutningen till databasen |
| `analys.ipynb` | Datakvalitet, diagram och svar |
| `requirements.txt` | Paketen som behövs |
| `.gitignore` | Filer som inte ska till GitHub |
| `.env` | Inloggningen. Finns bara på min dator |

## Data

| Tabell | Eurostat | Innehåll |
|---|---|---|
| `arbetsloshet` | `une_rt_a` (sex T, age Y25-74, unit PC_ACT) | Arbetslöshet i procent, 25-74 år |
| `utbildning` | `edat_lfse_03` (sex T, age Y25-64, isced11 ED5-8, unit PC) | Andel högskoleutbildade i procent, 25-64 år |

Båda tabellerna har kolumnerna `land`, `ar` och `varde`. Eurostat använder EL för Grekland.

## Så kör man det (Kommandotolken i Windows)

```
py -V:3.13 -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

Skapa filen `.env` med en rad. Byt orden med stora bokstäver mot egna uppgifter:

```
DB_URL=mysql+pymysql://ANVANDARNAMN:LOSENORD@SERVER:PORT/DATABASNAMN
```

Databasen måste finnas. Kör sedan:

```
python db.py
python kor.py
```

Öppna `analys.ipynb` i VS Code, välj `.venv` och klicka på Run All.

### Visa resultaten som en lokal hemsida

```
python -m nbconvert --to html --no-input analys.ipynb
start analys.html
```

Det skapar `analys.html` med diagram, tabeller och svar, utan kod. Sidan visar det som är sparat
i notebooken.

## Slutsatser (år 2025)

Siffrorna hämtades 26 november 2026. Eurostat kan ändra dem senare.

**Fråga 1:** Svårast att få jobb var det i Spanien (9,4 % arbetslöshet), sedan Grekland (8,3 %) och
Finland (8,1 %). Lägst var Tjeckien (2,3 %). Medianen för EU:s länder var 5,0 %.

**Fråga 2:** Jag ser inget tydligt samband. Spearman är 0,26. Lutningen är 0,033 med 95 %
konfidensintervall -0,046 till 0,112, alltså innehåller det 0. Det är ett samband mellan länder
och inte en orsak.

**Begränsning:** arbetslösheten gäller 25-74 år och utbildningen 25-64 år.

## Metoder och commits

| Commit | Meddelande | Metod och vad den visar |
|---|---|---|
| `868bebf` | Lägg till .gitignore | Hemliga filer kommer inte med |
| `bd00591` | Lägg till requirements.txt med paketversioner | Samma paket kan installeras igen |
| `089d582` | Lägg till db.py för anslutningen till databasen | Anslutning utan lösenord i koden |
| `aa1479d` | Hämta arbetslöshet till tabellen arbetsloshet | Hämtning från Eurostat och lång tabell |
| `b31e8f1` | Dela upp koden i hämta, rensa, spara och kör | En fil för varje steg |
| `ddcdc55` | Hämta utbildning till tabellen utbildning | Samma flöde för ett till dataset |
| `93ffee0` | Lägg till analysen i en notebook | Datakvalitet, stapeldiagram, Spearman, regression |
| `1be4df0` | Lägg till README.md | Beskrivning av projektet |
| `0adbddb` | Lägg till tabeller för resultaten | Tabeller med alla länder och svaren |

README uppdaterades i commiten efter dessa.

## Värden att kontrollera på Eurostats webbplats (år 2025)

| Värde | Dataset | Val | Enligt databasen |
|---|---|---|---|
| Arbetslöshet, Spanien | [une_rt_a](https://ec.europa.eu/eurostat/databrowser/view/une_rt_a/default/table?lang=en) | Total, 25-74 år, % of labour force | 9,4 |
| Arbetslöshet, Tjeckien | samma | samma | 2,3 |
| Högskoleutbildade, Sverige | [edat_lfse_03](https://ec.europa.eu/eurostat/databrowser/view/edat_lfse_03/default/table?lang=en) | Total, 25-64 år, Tertiary education (levels 5-8) | 50,8 |
