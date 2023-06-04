from forex_python.converter import CurrencyRates #type: ignore
import gspread #type: ignore

# service account definiálás
sa = gspread.service_account()

# doc és worksheet definiálás
sh = sa.open("ExchangeRates") 
wks = sh.worksheet("RateSheet")

# árfolyam lekérő algoritmus
def get_currency_rate(from_currency, to_currency):
    c = CurrencyRates()

    amount = 1
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    try:
        result = c.convert(from_currency, to_currency, amount)
        rounded_result = round(result, 3)
        return rounded_result
    except Exception as e:
        print(f"hiba az átváltáskor: {str(e)}")

# Munkafüzet sorainak hossza
num_rows = len(wks.get_all_values())

# Végig megy minden soron
for row in range(2, num_rows + 1): # Az első a fejléc
    moneyfrom = wks.cell(row, 1).value
    moneyto = wks.cell(row, 2).value
    rate = get_currency_rate(moneyfrom, moneyto)

    # Frissiti a dokumentumot és kiírja az aktuális értékeket
    wks.update_cell(row, 3, rate)
    print(f"Árfolyam frissítve: {moneyfrom} -> {moneyto} : {rate}")

print("Az árfolyamok frissítése sikeresen megtörtént.")