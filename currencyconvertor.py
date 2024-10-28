from forex_python.converter import CurrencyRates

def currency_converter(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

# Example usage
amount = 100
from_currency = 'USD'
to_currency = 'EUR'

result = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is {result} {to_currency}")
