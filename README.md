///// Telepítés

1. virtuális környezet telepítése és aktiválása

python -m venv venv

venv\Scripts\activate

2. szükséges modulok telepítése

pip install -r requirements.txt

///// Használat
1_currency_converter.py

forex_python segítségével
A működéshez internet kapcsolat szükséges

1. Váltandó mennyiség megadása
2. Kezdeti pénznem megadása
3. Cél pénznem megadása

A program kiírja az átváltott pénzmennyiséget a forex árfolyamok alapján

---

2_password_generator.py
python secrets modul segítségével

1. Karakterhossz megadása
2. Tartalmazzon-e számokat
3. Tartalmazzon-e speciális karaktereket

A program kiírja a paraméterek alapján generált jelszót

---

3_google_sheet.py
frontex, és gspread modul segítségével

Beolvassa a google sheetben szereplő pénznemeket és frissíti a táblázatban az átváltási rátájukat a frontexből lekért adatok alapján.
Az aktuálius értékeket kiírja a consolra is.

A service_account.json sensitive adat (nem kerül bele a repoba).
A service_account.json file helye:
Windows: %APPDATA%\gspread
Linux: ~./config/gspread
