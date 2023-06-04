from forex_python.converter import CurrencyRates #type: ignore

def currency_converter():
    c = CurrencyRates() #lekéri a forex árfolyamokat (a forex nem kér API keyt)

    amount = float(input("Add meg az összeget: "))
    from_currency = input("Add meg milyen pénznemet szeretnél átváltani: ").upper()
    to_currency = input("Add meg mire szeretnél váltani: ").upper()

    try:
        result = c.convert(from_currency, to_currency, amount) #elvégzi az átváltást
        rounded_result = round(result, 3) #lekerekíti az ereményt 3 tizedesjegyre
        print(f"\n{amount} {from_currency} = {rounded_result} {to_currency}")
    except Exception as e:
        print(f"hiba az átváltáskor: {str(e)}")

currency_converter()